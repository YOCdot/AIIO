# ---*--- File Information ---*---
# @File       :  models.py
# @Date&Time  :  2023-01-06, 14:31:25
# @Project    :  AIIO
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


import os
import numpy as np

import onnx
import onnxruntime as ort
import cv2
import torch
import torchvision
import torchvision.transforms as T

from .cat_mapping import coco2017_mapping


class Normalize(object):
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, image, target=None):
        image = torchvision.transforms.functional.normalize(image, mean=self.mean, std=self.std)
        return image


class ONNXModel:
    """ ONNX + ONNXRuntime 推理 """

    def __init__(self, name, scale, path_url="./onnx_ptw", print_repr=False):

        self.name = name  # 模型名称
        self.scale = scale  # 模型规模

        self.pt_url = path_url + "/" + name + "_" + scale + ".onnx"
        self.onnx_verify(print_repr=print_repr)

        # 输入大小
        if name == "fpdt":
            self.input_size = 640
        elif name == "tssd":
            self.input_size = 672
        else:
            raise ValueError("`image_size` unmatch!")

        # 变换
        self.transform = T.Compose([T.ToTensor(),
                                    T.Resize((self.input_size, self.input_size)),
                                    Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        self.input = None  # 输入数据
        self.original_size = None  # 图片原始大小
        self.outputs = None  # 输出
        self.mapping = coco2017_mapping

    def __str__(self):
        return f"{str(self.name)}-{str(self.scale)} onnx model"

    def onnx_verify(self, print_repr=False):
        """ 检查模型是否正确加载 """

        # 加载 onnx 模型 + 检查模型格式是否正确组织
        onnx.checker.check_model(onnx.load(self.pt_url))

        # 打印可阅读的计算图表示
        if print_repr:
            print(onnx.helper.printable_graph(model.graph))

    def load_image(self, input_url):
        """ 加载 + 变换 """
        # import imagesize
        # print(imagesize.get(input_url))
        img_cv2 = cv2.imread(input_url)  # [H, W, C]
        self.original_size = (img_cv2.shape[1], img_cv2.shape[0])  # [H, W, C] -> [W, H]
        self.input = self.transform(img_cv2).unsqueeze(0).numpy()  # [C, H, W] -> [B, C, H, W]

    def get_raw_output(self):
        """ 获取生预测 """

        if self.input is None:
            raise ValueError("No input!")

        ort_session = ort.InferenceSession(self.pt_url)
        self.outputs = ort_session.run(
            None,
            {"input": self.input},
        )

    def bbox_convertor(self, coordinate, converting='plt'):
        """ 将模型输出的原始框格式从`cxcybwbh`转换位其他格式
        : param canvas:
            - 'plt': (cx, cy, bw, bh) => (lbx, lby, w, h)
            - 'cv2': (cx, cy, bw, bh) => (ltx, lty, rbx, rby)
        """

        if coordinate.shape[0] != 4:
            raise ValueError("Box coordinate error!")

        if converting == 'plt':
            cx, cy, bw, bh = coordinate
            lbx = ((cx - 0.5 * bw) * self.original_size[0]).item()
            lby = ((cy - 0.5 * bh) * self.original_size[1]).item()
            w = (bw * self.original_size[0]).item()
            h = (bh * self.original_size[1]).item()
            return [lbx, lby, w, h]
        elif converting == 'cv2':
            cx, cy, bw, bh = coordinate
            ltx = ((cx - 0.5 * bw) * self.original_size[0]).item()
            lty = ((cy - 0.5 * bh) * self.original_size[1]).item()
            rbx = ((cx + 0.5 * bw) * self.original_size[0]).item()
            rby = ((cy + 0.5 * bh) * self.original_size[1]).item()
            return [ltx, lty, rbx, rby]
        else:
            raise ValueError("No such format: `{}`!".format(converting))

    def wash_outputs(self, converting="plt"):
        """ 清洗生输出 """
        if self.outputs is None:
            raise ValueError("No outputs!")

        for out in self.outputs:
            if out.shape[-1] == 92:
                label = out.squeeze(0)
                label = np.argmax(label, axis=-1)
                # print(label)
            elif out.shape[-1] == 4:
                bbox = out.squeeze(0)
                # print(bbox)
            else:
                raise ValueError("Output error!")
            # print(type(out))
            # print(out.shape)

        output_dict = {}
        for idx, cat in enumerate(label):
            if cat != 91:
                # output_dict[self.mapping[str(cat)]] = self.bbox_convertor(bbox[idx].tolist())
                output_dict[self.mapping[str(cat)]] = self.bbox_convertor(bbox[idx], )
                # print(bbox[idx].tolist(), " => ", self.bbox_convertor(bbox[idx]))
        self.outputs = output_dict

    def inference(self, input_url, converting="plt"):

        # 1: 准备图片 => self.input
        self.load_image(input_url=input_url)

        # 2: 获取生输出
        self.get_raw_output()

        # 3: 清洗生输出 => 转化成画布可读格式
        self.wash_outputs(converting=converting)

        return self.outputs


if __name__ == '__main__':
    model = ONNXModel(name='fpdt', scale='tiny', path_url="./onnx_ptw")
    out_dict = model.inference(input_url="./dog-test.jpg")
    # print(len(out_dict), out_dict)

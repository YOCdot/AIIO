# ---*--- File Information ---*---
# @File       :  verify.py
# @Date&Time  :  2023-01-06, 16:21:45
# @Project    :  AIIO
# @Platform   :  Apple ARM64
# @Software   :  PyCharm
# @Author     :  yoc
# @Email      :  yyyyyoc@hotmail.com


import io
import numpy as np

import onnx
import onnxruntime as ort


def onnx_verify(weight_path="./onnx_ptw/fpdt_tiny.onnx", print_rep=False):
    """ 检查模型是否正确加载 """

    # 1. 加载 onnx 模型
    model = onnx.load(weight_path)

    # 2. 检查模型格式是否正确组织
    onnx.checker.check_model(model)

    # 3. 打印可阅读的计算图表示
    if print_rep:
        print(onnx.helper.printable_graph(model.graph))


def ort_verify(weight_path="./onnx_ptw/fpdt_tiny.onnx", print_rep=False):

    if not weight_path:
        raise ValueError("`weight_path`参数为空")

    ort_session = ort.InferenceSession(weight_path)

    outputs = ort_session.run(
        None,
        {"fpdtTinyInput": np.random.randn(1, 3, 640, 640).astype(np.float32)},
    )

    if print_rep:
        print(type(outputs), len(outputs))
        for out in outputs:
            print(type(out), out.shape)


def main():
    """

    FPDT
        TINY
            - fpdt_tiny.onnx
            - input_names: fpdtTinyInput
            - output_names: fpdtTinyOutput
        SMALL
            - fpdt_small.onnx
            - input_names: fpdtSmallInput
            - output_names: fpdtSmallOutput

    TSSD
        TINY
            - tssd_tiny.onnx
            - input_names: tssdTinyInput
            - output_names: tssdTinyOutput
        SMALL
            - tssd_small.onnx
            - input_names: tssdSmallInput
            - output_names: tssdSmallOutput

    """

    onnx_verify()
    ort_verify(print_rep=True)


if __name__ == '__main__':

    main()

<p align="center"><a href="https://iyoc.xyz/" target="_blank" rel="noopener noreferrer"><img width="200" src="assets/logo/white-logo-hires.png" alt="AIIO logo"></a></p>

<h1 align="center">Object Detection Online!</h1>

<p align="center">
  <a href="https://github.com/vuejs/vue"><img src="https://img.shields.io/badge/Vue-3.0%2B-65b687" alt="Vue"></a>
  <a href="https://github.com/axios/axios"><img src="https://img.shields.io/badge/Axios-1.2%2B-542cdb" alt="Axios"></a>
  <br />  
  <a href="https://github.com/django/django"><img src="https://img.shields.io/badge/Django-4.0%2B-214a35" alt="Django"></a>
  <a href="https://github.com/encode/django-rest-framework"><img src="https://img.shields.io/badge/DRF-3.14%2B-951d12" alt="Django Restful Framework"></a>
  <br />
  <a href="https://github.com/onnx/onnx"><img src="https://img.shields.io/badge/ONNX-1.12%2B-FEFEFE" alt="ONNX"></a>
  <a href="https://github.com/microsoft/onnxruntime"><img src="https://img.shields.io/badge/ONNXRuntime-1.11%2B-FEFEFE" alt="ONNX Runtime"></a>
</p>

# Deployment

## Backend

Dev port: `http://localhost:8000/`

```shell
conda activate backend

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

## Frontend

Dev port: `http://localhost:5173/`

```shell
cd frontend

npm install

npm run dev
```

FROM nvcr.io/nvidia/tensorflow:22.04-tf2-py3 
ENV PYTHONUNBUFFERED True

RUN apt-get update \
    && apt-get install -y python3-tk \
    && apt-get install ffmpeg libsm6 libxext6 -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install torch==1.10.0+cu111 torchvision==0.11.1+cu111 torchtext==0.11.0 -f https://download.pytorch.org/whl/torch_stable.html --upgrade 
RUN pip install mmcv-full==1.3.17 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.10.0/index.html --upgrade
RUN pip install mmdet==2.17.0 --upgrade
RUN pip install mmsegmentation==0.20.2 --upgrade
RUN pip install git+https://github.com/airctic/icevision.git#egg=icevision[all] --upgrade
RUN pip install git+https://github.com/airctic/icedata.git --upgrade

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

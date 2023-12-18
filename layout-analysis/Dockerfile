FROM python:3.11
ENV PYTHONUNBUFFERED True

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# torch has to be installed before installing layoutparser
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install -U layoutparser
RUN pip3 install 'git+https://github.com/facebookresearch/detectron2.git@v0.4#egg=detectron2'

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
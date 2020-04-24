FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64

RUN apt update && apt install -y wget build-essential cmake \
    libsm6 libfontconfig1 libxrender1 libxtst6 libopenblas-dev liblapack-dev \
    libglib2.0-0 libgtk2.0-dev libzbar0 python3.7-dev git

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.7 get-pip.py

COPY requirements.txt requirements.txt
RUN pip3.7 install -r requirements.txt

RUN git clone https://www.github.com/nvidia/apex
RUN pip3.7 install -e "apex" --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext"

COPY . .
WORKDIR /

CMD ["python3.7", "bot.py"]

FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3-pip

RUN pip3 install --user kaggle pandas scikit-learn sklearn

ENV PATH="/root/.local/bin:${PATH}"

COPY data_processing.sh .

WORKDIR .
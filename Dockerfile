FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install kaggle pandas scikit-learn

COPY data_processing.sh .

WORKDIR .
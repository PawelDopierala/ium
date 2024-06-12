FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install pandas scikit-learn tensorflow sacred pymongo --break-system-packages GitPython

RUN useradd -ms /bin/bash jenkins

RUN mkdir -p /.kaggle && chown -R jenkins /.kaggle

USER jenkins

COPY data_processing.py .
COPY create_model.py .
COPY helper.py .
COPY evaluate.py .

WORKDIR .
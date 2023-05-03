FROM python:3.8-slim

# 今回はpoetryなどは面倒なので使わない
RUN pip install --upgrade pip \
    && pip install grpcio \
    && pip install grpcio-tools

WORKDIR /src
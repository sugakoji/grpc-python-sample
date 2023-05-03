FROM python:3.8-slim

# 面倒なので
RUN pip install --upgrade pip \
    && pip install grpcio \
    && pip install grpcio-tools


FROM python:3.11-slim

WORKDIR /app

RUN pip install minio

COPY src ./src

CMD ["python", "src/common/storage/create_buckets.py"]
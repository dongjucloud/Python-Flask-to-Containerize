# Dockerfile
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV NAME Game

CMD ["python3", "app.py"]

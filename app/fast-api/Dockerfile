FROM python:3.13-alpine

RUN apk update && apk add --no-cache \
    gcc \
    mariadb-connector-c \
    mariadb-dev \
    musl-dev

WORKDIR /app
COPY quiminhoca-backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY quiminhoca-backend/src/ ./src
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

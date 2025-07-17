FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev  \
    libmariadb3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
# COPY ../../.env .
COPY quiminhoca-backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY quiminhoca-backend/src/ ./src
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Remove Expose to prod
EXPOSE 8000 

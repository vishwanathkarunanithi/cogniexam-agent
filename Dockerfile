# Production-Grade Container for Google Cloud Run / AWS ECS
FROM python:3.11-slim

# Prevent Python from writing .pyc and enable bufferless logging
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Expose standard Cloud Run port
EXPOSE 8080

# Run Streamlit on container launch
HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health || exit 1
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.enableCORS=false"]


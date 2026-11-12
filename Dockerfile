# Production-Grade Container for Hugging Face Spaces / Cloud Run
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=7860

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user (UID 1000) standard for Hugging Face Spaces
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app
COPY --chown=user:user . .

EXPOSE 7860

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "7860"]

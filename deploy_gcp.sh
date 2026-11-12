#!/usr/bin/env bash
# 1-Click Deployment Script to Google Cloud Run (Linux / Mac / GCP Cloud Shell)
set -e

echo "=========================================================="
echo " CogniExam: Google Cloud Run 1-Click Deployer"
echo "=========================================================="

PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo "No active GCP project detected. Please enter your Google Cloud Project ID:"
    read -r PROJECT_ID
    gcloud config set project "$PROJECT_ID"
fi
echo "[✓] Active GCP Project: $PROJECT_ID"

REGION="us-central1"
SERVICE_NAME="cogniexam-agent"

echo "[*] Enabling required Google Cloud APIs..."
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com aiplatform.googleapis.com storage.googleapis.com

echo "[*] Building and deploying to Cloud Run..."
gcloud run deploy "$SERVICE_NAME" \
    --source . \
    --region "$REGION" \
    --platform managed \
    --allow-unauthenticated \
    --memory 2Gi \
    --cpu 2 \
    --timeout 300

echo "=========================================================="
echo " [SUCCESS] Application is now live on Google Cloud Run!"
echo "=========================================================="
gcloud run services describe "$SERVICE_NAME" --region "$REGION" --format='value(status.url)'


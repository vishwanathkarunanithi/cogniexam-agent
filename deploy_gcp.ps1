# 1-Click Deployment Script to Google Cloud Run (Windows PowerShell)
$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " CogniExam: Google Cloud Run 1-Click Deployer" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Check GCP Project
$PROJECT_ID = gcloud config get-value project 2>$null
if (-not $PROJECT_ID) {
    Write-Host "No active GCP project detected. Please enter your Google Cloud Project ID:" -ForegroundColor Yellow
    $PROJECT_ID = Read-Host "Project ID"
    gcloud config set project $PROJECT_ID
}
Write-Host "[OK] Active GCP Project: $PROJECT_ID" -ForegroundColor Green

$REGION = "us-central1"
$SERVICE_NAME = "cogniexam-agent"

# 2. Enable APIs
Write-Host "[*] Enabling required Google Cloud APIs (Cloud Run, Cloud Build, Artifact Registry, Vertex AI)..." -ForegroundColor Yellow
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com aiplatform.googleapis.com storage.googleapis.com

# 3. Build & Deploy using Cloud Build and Cloud Run
Write-Host "[*] Submitting source code to Google Cloud Build and deploying to Cloud Run..." -ForegroundColor Yellow
gcloud run deploy $SERVICE_NAME `
    --source . `
    --region $REGION `
    --platform managed `
    --allow-unauthenticated `
    --memory 2Gi `
    --cpu 2 `
    --timeout 300

Write-Host "==========================================================" -ForegroundColor Green
Write-Host " [SUCCESS] Application is now live on Google Cloud Run!" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
gcloud run services describe $SERVICE_NAME --region $REGION --format="value(status.url)"


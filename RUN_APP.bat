@echo off
title CogniExam - AI Smart Examination & Bloom's Assessment Agent (React Native Web)
color 0B

echo =====================================================================
echo  AI-Driven Smart Examination Design & Bloom's Assessment Agent
echo  High-Performance Multi-Agent Platform (FastAPI + React Native Web)
echo =====================================================================
echo.
echo [1/3] Verifying Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not detected in your PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    echo.
    pause
    exit /b
)

echo [2/3] Checking dependencies...
pip install -r requirements.txt --quiet --disable-pip-version-check

echo [3/3] Launching CogniExam Server on http://localhost:8000...
echo.
echo =====================================================================
echo  Opening browser at http://localhost:8000
echo  Press Ctrl+C in this terminal window anytime to stop the server.
echo =====================================================================
echo.

start "" "http://localhost:8000"
python -m uvicorn server:app --host 0.0.0.0 --port 8000

pause

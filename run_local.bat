@echo off
TITLE CogniExam - Autonomous Academic Assessment Agent
COLOR 0B
echo =========================================================================
echo               COGNIEXAM: AUTONOMOUS MULTI-AGENT OBE SYSTEM
echo                  Outcome-Based Education Academic Auditor
echo =========================================================================
echo.
echo [1/3] Checking Python runtime...
python --version
if errorlevel 1 (
    echo [ERROR] Python 3.10+ is required but not found in PATH.
    pause
    exit /b 1
)

echo.
echo [2/3] Checking dependencies...
python -c "import fastapi, uvicorn, reportlab, google.genai" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing required dependencies...
    pip install -r requirements.txt
)

echo.
echo [3/3] Starting CogniExam Server on http://localhost:8000 ...
echo [INFO] Direct browser link: http://localhost:8000
echo.
start http://localhost:8000
python -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
pause


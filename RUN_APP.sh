#!/usr/bin/env bash
# CogniExam Launcher for macOS and Linux
set -e

echo "====================================================================="
echo " AI-Driven Smart Examination Design & Bloom's Assessment Agent"
echo "====================================================================="
echo ""

if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 could not be found. Please install Python 3.10+."
    exit 1
fi

echo "[1/3] Python detected."
echo "[2/3] Installing requirements..."
pip3 install -r requirements.txt --quiet

echo "[3/3] Launching CogniExam on http://localhost:8501..."
python3 -m streamlit run app.py --server.port 8501


"""
Quick Diagnostic Tool to verify Cloud AI Connection.
Run this script to test live connectivity to Google Gemini / Vertex AI.
"""

import os
import sys
from core.cloud_client import CloudAgentClient

def main():
    print("=" * 60)
    print(" CogniExam Cloud AI Connectivity Test")
    print("=" * 60)
    
    client = CloudAgentClient()
    print(f"[*] Detected Connection Mode: {client.mode.upper()}")
    
    if client.is_cloud_connected():
        print("[✓] Successfully connected to Google Cloud AI!")
        print("[*] Sending test prompt to verify Bloom's reasoning...")
        try:
            resp = client.generate_completion(
                "Define Bloom's Revised Taxonomy Level 4 (Analyze) in one concise sentence."
            )
            print("\n[AI Response from Cloud]:")
            print(resp.strip())
            print("\n[✓] Cloud AI Integration is 100% LIVE and WORKING!")
        except Exception as e:
            print(f"[!] Error during model execution: {e}")
    else:
        print("[!] No active Cloud API key or GCP project credentials detected.")
        print("[*] The system is currently operating in 'Autonomous Local Heuristic' mode.")
        print("    (It works offline with built-in Bloom's balancing & rubric evaluation).")
        print("\nTo activate live Google Cloud AI:")
        print("  1. Get a free API key from https://aistudio.google.com/apikey")
        print("  2. Run: setx GEMINI_API_KEY \"your_api_key_here\"")
        print("  3. Re-run this test script.")

if __name__ == "__main__":
    main()


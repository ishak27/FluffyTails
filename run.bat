@echo off
title FluffyTails Pet Adoption System
cd /d "%~dp0"

echo ===================================================
echo     Starting FluffyTails Pet Adoption System
echo ===================================================
echo.

if not exist "venv\Scripts\python.exe" (
    echo [!] Windows virtual environment not found. Setting up...
    py -3.12 -m venv venv 2>nul || python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Python installation not found. Please install Python 3.10+ from python.org.
        pause
        exit /b 1
    )
    echo [*] Installing dependencies from requirements.txt...
    venv\Scripts\pip install -r requirements.txt
)

echo [*] Launching Flask web server on http://127.0.0.1:5000 ...
echo [*] Default Admin Login: admin@gmail.com / admin123
echo [*] Press Ctrl+C in this window to stop the server.
echo.
venv\Scripts\python.exe app.py

pause

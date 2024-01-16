@echo off
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Opening download link...
    start https://www.python.org/downloads/release/python-3117/
    exit /b
)
cd .env\Scripts
call activate.bat
cd ../..
python.exe main.py
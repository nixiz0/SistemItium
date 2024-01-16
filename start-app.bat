@echo off
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Opening download link...
    start https://www.python.org/downloads/release/python-3117/
) else (
    echo Python is installed.
)

where git >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Opening download link...
    start https://git-scm.com/downloads
) else (
    echo Git is installed.
)

where code >nul 2>&1
if errorlevel 1 (
    echo VSCode is not installed. Opening download link...
    start https://code.visualstudio.com/download
) else (
    echo VSCode is installed.
)

cd .env\Scripts
call activate.bat
cd ../..
python.exe main.py
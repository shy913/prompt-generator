@echo off
echo Starting AI Prompt Generator...

REM Check if venv directory exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Check if streamlit is installed
python -c "import streamlit" 2>NUL
if %ERRORLEVEL% NEQ 0 (
    echo Installing required packages...
    pip install streamlit
)

REM Run the application
python run.py

REM The virtual environment will be automatically deactivated when the batch file exits

@echo off
echo Starting GitHub Push Utility...

REM Check if venv directory exists, if not create it
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Run the push to GitHub script
python push_to_github.py

REM Deactivate the virtual environment
call venv\Scripts\deactivate.bat

echo.
echo Press any key to exit...
pause > nul
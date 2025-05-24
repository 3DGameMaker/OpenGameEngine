py get-pip.py
pip install -r requirements.txt
pyinstaller --onefile C:\Users\vanhu\AppData\Local\Programs\OpenGameEngine\OGE0.1\oge.py
@echo off
:: This adds to the current USER's PATH (no admin needed)
set "NEW_PATH=C:\Users\vanhu\AppData\Local\Programs\OpenGameEngine\OGE0.1\dist"

:: Check if already in PATH
echo %PATH% | find /i "%NEW_PATH%" > nul
if %errorlevel% equ 0 (
    echo [INFO] "%NEW_PATH%" is already in PATH.
    pause
    exit /b
)

:: Add to PATH permanently
setx PATH "%PATH%;%NEW_PATH%"

echo [SUCCESS] Added "%NEW_PATH%" to PATH. Restart CMD to see changes.
pause
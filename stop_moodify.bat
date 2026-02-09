@echo off
echo Stopping Moodify...

taskkill /F /IM uvicorn.exe >nul 2>&1
taskkill /F /IM streamlit.exe >nul 2>&1

echo Moodify Stopped
pause

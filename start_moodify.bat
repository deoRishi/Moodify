@echo off
echo Starting Moodify...

call moodenv\Scripts\activate

REM Start Backend
start cmd /k "cd backend && uvicorn main:app --reload"

REM Wait
timeout /t 3

REM Start Frontend
start cmd /k "cd frontend && streamlit run app.py"

echo Moodify Started
pause

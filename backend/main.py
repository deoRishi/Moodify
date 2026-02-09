from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from datetime import datetime

# ---------------------------
# Initialize App
# ---------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Load Emotion Model
# ---------------------------

model = load_model("emotion_model.h5")

emotions = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Sad",
    "Surprise",
    "Neutral"
]

# ---------------------------
# Home Route
# ---------------------------

@app.get("/")
def home():
    return {"message": "Moodify API Running"}

# ---------------------------
# Predict Emotion
# ---------------------------

@app.post("/predict")
async def predict_emotion(file: UploadFile = File(...)):
    contents = await file.read()

    img = Image.open(io.BytesIO(contents)).convert("L")
    img = img.resize((48, 48))

    img = np.array(img) / 255.0
    img = img.reshape(1, 48, 48, 1)

    prediction = model.predict(img)
    emotion = emotions[np.argmax(prediction)]

    return {"emotion": emotion}

# ---------------------------
# Save Feedback
# ---------------------------

@app.post("/feedback")
async def save_feedback(
    emotion: str = Form(...),
    feedback: str = Form(...)
):
    time = datetime.now().isoformat()

    with open("../feedback/feedback.csv", "a") as f:
        f.write(f"{time},{emotion},{feedback}\n")

    return {"status": "saved"}

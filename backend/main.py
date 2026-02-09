from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from datetime import datetime
import cv2

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
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

model = load_model("emotion_model.h5")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


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

    image = Image.open(io.BytesIO(contents)).convert("RGB")
    img_np = np.array(image)
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    if len(faces) == 0:
        return {"error": "No face detected"}

    x, y, w, h = faces[0]
    face = gray[y:y+h, x:x+w]
    face = cv2.resize(face, (48,48))
    face = face / 255.0
    face = face.reshape(1,48,48,1)

    pred = model.predict(face)
    emotion = emotions[np.argmax(pred)]

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

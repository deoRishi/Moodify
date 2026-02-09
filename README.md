\# 🎧 Moodify — AI Mood-Based Music Recommender



Moodify is an end-to-end AI-powered web application that detects a user's facial emotion using deep learning and recommends music based on their mood.



---



\## 🔥 Features



\- Facial emotion detection using CNN

\- Webcam-based image capture

\- Real-time emotion classification

\- Mood-based Spotify playlist recommendation

\- User feedback collection

\- FastAPI backend

\- Streamlit frontend

\- Modular project structure

\- One-click start/stop scripts



---
flowchart TD
    A[User Webcam / Image Upload] --> B[Streamlit Frontend]
    B --> C[FastAPI Backend]
    C --> D[Face Detection - OpenCV Haar Cascade]
    D --> E[Emotion CNN Model]
    E --> C
    C --> F[Predicted Emotion]
    F --> G[Music Recommendation Logic]
    G --> B
    B --> H[User Feedback]
    H --> I[Feedback CSV Storage]

---

flowchart LR
    A[FER2013 Dataset] --> B[Preprocessing]
    B --> C[Image Normalization]
    C --> D[CNN Training]
    D --> E[Trained Emotion Model]
    E --> F[Saved as emotion_model.h5]
    F --> G[Loaded by Backend API]

---

\## 🧠 Tech Stack



\- Python 3.10  

\- TensorFlow / Keras  

\- OpenCV  

\- FastAPI  

\- Streamlit  

\- NumPy, Pandas  

\- Git \& GitHub  



---



\## 📁 Project Structure



Moodify/

│

├── backend/

│ └── main.py

│

├── frontend/

│ └── app.py

│

├── model/

│ └── train\_emotion\_model.ipynb

│

├── data/

│ └── fer2013/

│

├── feedback/

│ └── feedback.csv

│

├── start\_moodify.bat

├── stop\_moodify.bat

├── requirements.txt

└── README.md





---



\## ⚙️ Installation



```bash

python -m venv moodenv

moodenv\\Scripts\\activate

pip install -r requirements.txt





▶️ Run Application

start\_moodify.bat





Stop:

stop\_moodify.bat



📸 How It Works



Capture face using webcam



CNN predicts emotion



Backend returns emotion



Frontend shows result



Spotify playlist suggested



User provides feedback





📈 Future Improvements



Face detection before emotion classification



Transfer learning (ResNet/MobileNet)



User accounts



Cloud deployment



Advanced recommender system





👨‍💻 Author

@deoRishi

Email : deoghariarishikesh2005@gmail.com


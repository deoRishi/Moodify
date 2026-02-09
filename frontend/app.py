import streamlit as st
import requests
from PIL import Image

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Moodify")
st.title("🎧 Moodify - Emotion Based Music Recommender")

img = st.camera_input("Take a photo")

if img:
    st.image(img)
    
    if st.button("Analyze Mood"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                API_URL,
                files={"file": img.getvalue()}
            )
            result = response.json()
            emotion = result["emotion"]
            st.success(f"Detected Emotion: {emotion}")

            music = {
                "Happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
                "Sad": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
                "Angry": "https://open.spotify.com/playlist/37i9dQZF1DWYxwmBaMqxsl",
                "Neutral": "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",
                "Fear": "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO",
                "Surprise": "https://open.spotify.com/playlist/37i9dQZF1DX5wDmLW735Yd",
                "Disgust": "https://open.spotify.com/playlist/37i9dQZF1DX59CJ8da3Yxk"
            }

            st.markdown(f"[Open Music Playlist]({music[emotion]})")

            st.subheader("Was this recommendation helpful?")
            
            col1, col2 = st.columns(2)
            if col1.button("👍 Yes"):
                requests.post(
                    "http://127.0.0.1:8000/feedback",
                    params={"emotion":emotion,"feedback":"good"}
                )
                st.success("Thanks for your feedback!")

            if col2.button("👎 No"):
                requests.post(
                    "http://127.0.0.1:8000/feedback",
                    params={"emotion":emotion,"feedback":"bad"}
                )
                st.success("Thanks for your feedback!")

import streamlit as st
from gtts import gTTS

st.title("🎙️ Wambi Voice Test")

# Voice message
message = "Robin, Wambi is ready to serve you."

# Generate speech
tts = gTTS(text=message, lang='en')
tts.save("wambi_test.mp3")

# Play voice message
st.audio("wambi_test.mp3", format="audio/mp3")

import streamlit as st
from datetime import datetime

# User Name
user_name = "Hard Guy"  # You can make this dynamic later

# Header
st.title(f"👋 Hey Wambi, it's me")
st.markdown(f"### Wambi, remember the words of your Father")

# Wake message
st.success("“Wake up, Hard Guy. Greatness never sleeps.”")

# Daily quote (you can make this rotate later)
st.info("💬 *'Discipline is the bridge between goals and accomplishment.'*")

# Vital scan placeholder
st.markdown("---")
st.subheader("📊 Morning Vital Scan (coming soon)")
st.write("Wambi will check your vitals using your webcam and smart sensors.")

# Face recognition placeholder
st.subheader("📸 Face Recognition (coming soon)")
st.write("Face ID will personalize the experience for you, Hard Guy.")

# Voice assistant placeholder
st.subheader("🎙️ Voice Assistant (coming soon)")
st.write("You will soon be able to talk to Wambi using your voice.")

# Footer
st.markdown("---")
st.caption(f"🕒 {datetime.now().strftime('%A, %B %d, %Y - %H:%M:%S')}")
st.caption("Powered by Streamlit | Wambi AI (Preview)")
import streamlit as st

st.title("Hello from Wambi!")

st.write("If you see this, Streamlit is running.")
import streamlit as st
import cv2
from gtts import gTTS

st.title("🔍 Wambi Face Detection + Vital Scan")

run = st.button("Scan My Face")

if run:
    st.write("📷 Scanning webcam... Please hold still.")

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("Camera not accessible.")
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) > 0:
            st.success("Face detected ✅")
            message = "Hard Guy, your identity has been confirmed. Let’s check your vitals."
        else:
            st.error("No face detected ❌")
            message = "No face detected, please try again."

        tts = gTTS(message)
        tts.save("wambi_voice.mp3")
        st.audio("wambi_voice.mp3", format="audio/mp3")

        st.image(frame, channels="BGR", caption="Webcam Snapshot")



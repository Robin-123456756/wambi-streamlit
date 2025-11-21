import streamlit as st
from gtts import gTTS
import random
import speech_recognition as sr
import tempfile
from datetime import datetime
import numpy as np
from scipy.io.wavfile import write
from streamlit_audio_recorder import audio_recorder

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Wambi AI", page_icon="🌞")

# --- HEADER ---
st.title("🌞 Good Morning, Hard Guy")
st.markdown("### Wambi, remember the words of your Father")
st.success("“Wake up, Hard Guy. Greatness never sleeps.”")
st.info("💬 *'Discipline is the bridge between goals and accomplishment.'*")
st.markdown("---")

# --- START MY DAY SECTION ---
if st.button("Start My Day", key="start_day"):
    st.success("✅ Wambi Activated")

    # -- Greeting Audio --
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    # -- Simulated Vital Signs --
    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])
    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")

    # -- Coffee Sugar Recommendation --
    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")

    # -- Exercise Tip --
    st.subheader("🏋️‍♂️ Exercise Tip")
    tip = random.choice([
        "20-minute morning walk",
        "15-minute yoga stretch",
        "10 push-ups, 20 squats",
        "High-Intensity 5-minute HIIT"
    ])
    st.write(f"Today’s suggestion: **{tip}**")

    # -- Farewell Audio --
    farewell = "All set, Hard Guy. Crush the day."
    tts = gTTS(farewell)
    tts.save("farewell.mp3")
    st.audio("farewell.mp3", format="audio/mp3")

st.markdown("---")

# --- LIVE MIC RECORDING USING streamlit_audio_recorder ---
st.subheader("🎤 Speak to Wambi (Live Microphone Recording)")

audio_bytes = audio_recorder()  # User records directly in browser
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # Convert audio bytes to numpy array for SpeechRecognition
    audio_np = np.frombuffer(audio_bytes, dtype=np.int16)
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_wav.name, 44100, audio_np)

    recognizer = sr.Recognizer()
    with sr.AudioFile(temp_wav.name) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        st.success(f"🗣️ You said: **{text}**")
    except sr.UnknownValueError:
        st.warning("Wambi couldn't understand that, Hard Guy.")
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")

st.markdown("---")

# --- VOICE COMMAND UPLOADER (OPTIONAL) ---
st.subheader("🎙️ Upload Voice Command")
uploaded_file = st.file_uploader(
    "Upload a .wav audio file (Max: 10MB)", type=["wav"], key="voice_upload"
)

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")

    # Transcribe uploaded file
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with sr.AudioFile(tmp_path) as source:
        audio_file = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_file)
        st.success(f"You said: {text}")
    except sr.UnknownValueError:
        st.warning("Sorry, Wambi could not understand the audio.")
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")

st.markdown("---")

# --- COMING SOON PLACEHOLDERS ---
st.subheader("📊 Morning Vital Scan (coming soon)")
st.write("Wambi will check your vitals using your webcam and smart sensors.")

st.subheader("📸 Face Recognition (coming soon)")
st.write("Face ID will personalize the experience for you, Hard Guy.")

st.subheader("🎙️ Voice Assistant (coming soon)")
st.write("You will soon be able to talk to Wambi using your voice.")

# --- FOOTER ---
st.markdown("---")
st.caption(f"🕒 {datetime.now().strftime('%A, %B %d, %Y - %H:%M:%S')}")
st.caption("Powered by Streamlit | Wambi AI (Preview)")

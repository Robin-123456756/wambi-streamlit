import streamlit as st
from gtts import gTTS
import random
import speech_recognition as sr
import tempfile
from datetime import datetime

# Set page config early
st.set_page_config(page_title="Wambi AI", page_icon="🌞")

# --- HEADER ---
st.title("🌞 Good Morning, Hard Guy")
st.markdown("### Wambi, remember the words of your Father.")

# --- BUTTON: Start My Day ---
if st.button("Start My Day", key="start_my_day"):
    st.success("✅ Wambi Activated")

    # Alarm greeting voice
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    # Simulated Vital Signs
    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])
    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")

    # Coffee sugar recommendation
    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")

    # Exercise tip suggestion
    st.subheader("🏋️‍♂️ Exercise Tip")
    tip = random.choice([
        "20-minute morning walk",
        "15-minute yoga stretch",
        "10 push-ups, 20 squats",
        "High-Intensity 5-minute HIIT"
    ])
    st.write(f"Today’s suggestion: **{tip}**")

    # Personalized farewell voice
    farewell = "All set, Hard Guy. Crush the day."
    tts = gTTS(farewell)
    tts.save("farewell.mp3")
    st.audio("farewell.mp3", format="audio/mp3")

# --- SEPARATOR ---
st.markdown("---")

# --- VOICE COMMAND UPLOADER ---
st.subheader("🎙️ Upload Voice Command")
uploaded_file = st.file_uploader("Upload a .wav audio file", type=["wav"], key="voice_upload")
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    recognizer = sr.Recognizer()
    with sr.AudioFile(tmp_path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        st.success(f"You said: {text}")
    except sr.UnknownValueError:
        st.warning("Sorry, I could not understand the audio.")
    except sr.RequestError:
        st.error("Speech recognition service is unavailable.")

# --- PLACEHOLDERS FOR FUTURE FEATURES ---
st.markdown("---")
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

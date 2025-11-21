import streamlit as st
from gtts import gTTS
import random
import speech_recognition as sr
import tempfile
from datetime import datetime
from streamlit.components.v1 import declare_component

# --- PAGE CONFIG ---
st.set_page_config(page_title="Wambi AI", page_icon="🌞", layout="wide")

# --- PINK THEME ---
st.markdown("""
<style>
body { background-color: #fff0f5; }
h1,h2,h3 { color: #ff1493; }
.card {
    background-color: #ffe4f1;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
button { background-color: #ff69b4; color: white; font-size:16px; padding:10px 20px; border-radius:12px; margin-right:10px; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>🌞 Good Morning, Hard Guy</h1>", unsafe_allow_html=True)
st.markdown("<h3>Wambi, remember the words of your Father</h3>", unsafe_allow_html=True)
st.success("“Wake up, Hard Guy. Greatness never sleeps.”")
st.info("💬 *'Discipline is the bridge between goals and accomplishment.'*")
st.markdown("---")

# --- START MY DAY ---
if st.button("Start My Day"):
    st.success("✅ Wambi Activated")

    # Greeting Audio
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    # Vitals
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])
    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")
    st.markdown('</div>', unsafe_allow_html=True)

    # Coffee
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")
    st.markdown('</div>', unsafe_allow_html=True)

    # Exercise
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🏋️‍♂️ Exercise Tip")
    tip = random.choice([
        "20-minute morning walk",
        "15-minute yoga stretch",
        "10 push-ups, 20 squats",
        "High-Intensity 5-minute HIIT"
    ])
    st.write(f"Today’s suggestion: **{tip}**")
    st.markdown('</div>', unsafe_allow_html=True)

    # Farewell Audio
    farewell = "All set, Hard Guy. Crush the day."
    tts = gTTS(farewell)
    tts.save("farewell.mp3")
    st.audio("farewell.mp3", format="audio/mp3")

st.markdown("---")

# --- LIVE MIC (Custom Component) ---
st.subheader("🎤 Speak to Wambi (Live Browser Mic)")

live_mic = declare_component("live_mic_component", path="./frontend")
audio_bytes = live_mic(key="live_mic")

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name
    recognizer = sr.Recognizer()
    with sr.AudioFile(tmp_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        st.success(f"🗣️ You said: **{text}**")
    except sr.UnknownValueError:
        st.warning("Wambi couldn't understand that, Hard Guy.")
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")

st.markdown("---")

# --- VOICE UPLOAD BACKUP ---
st.subheader("🎙️ Upload Voice Command")
uploaded_file = st.file_uploader("Upload a .wav audio file (Max: 10MB)", type=["wav"])
if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    recognizer = sr.Recognizer()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    with sr.AudioFile(tmp_path) as source:
        audio_file = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_file)
        st.success(f"🗣️ You said: {text}")
    except sr.UnknownValueError:
        st.warning("Sorry, Wambi could not understand the audio.")
    except sr.RequestError:
        st.error("Speech recognition service unavailable.")

st.markdown("---")

# --- COMING SOON ---
st.subheader("📊 Morning Vital Scan (coming soon)")
st.write("Wambi will check your vitals using your webcam and smart sensors.")

st.subheader("📸 Face Recognition (coming soon)")
st.write("Face ID will personalize the experience for you, Hard Guy.")

st.subheader("🎙️ Voice Assistant (coming soon)")
st.write("You will soon be able to talk to Wambi using your voice.")

# --- FOOTER ---
st.markdown("---")
st.caption(f"🕒 {datetime.now().strftime('%A, %B %d, %Y - %H:%M:%S')}")
st.caption("Powered by Streamlit | Wambi AI (Premium)")

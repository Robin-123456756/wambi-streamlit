import streamlit as st
from gtts import gTTS
import random
import speech_recognition as sr
import tempfile
from datetime import datetime
import base64
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Wambi AI", page_icon="🌞", layout="wide")

# --- STYLES FOR PINK THEME ---
st.markdown("""
<style>
body {
    background-color: #fff0f5;
}
h1, h2, h3 {
    color: #ff1493;
}
.stButton>button {
    background-color: #ff69b4;
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 160px;
    font-weight: bold;
    font-size: 16px;
}
.card {
    background-color: #ffe4f1;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1>🌞 Good Morning, Hard Guy</h1>", unsafe_allow_html=True)
st.markdown("<h3>Wambi, remember the words of your Father</h3>", unsafe_allow_html=True)
st.success("“Wake up, Hard Guy. Greatness never sleeps.”")
st.info("💬 *'Discipline is the bridge between goals and accomplishment.'*")
st.markdown("---")

# --- START MY DAY SECTION ---
if st.button("Start My Day", key="start_day"):
    st.success("✅ Wambi Activated")

    # Greeting Audio
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    # Simulated Vital Signs Card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])
    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")
    st.markdown('</div>', unsafe_allow_html=True)

    # Coffee Recommendation Card
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")
    st.markdown('</div>', unsafe_allow_html=True)

    # Exercise Tip Card
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

# --- FULLY AUTOMATIC LIVE MIC ---
st.subheader("🎤 Speak to Wambi (Live Browser Mic)")

# Embed HTML + JS component
components.html("""
<script>
let startBtn = document.createElement("button");
startBtn.innerHTML = "Start Recording";
let stopBtn = document.createElement("button");
stopBtn.innerHTML = "Stop Recording";
document.body.appendChild(startBtn);
document.body.appendChild(stopBtn);

let mediaRecorder;
let audioChunks = [];

startBtn.onclick = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    audioChunks = [];
    mediaRecorder.ondataavailable = e => audioChunks.push(e.data);
    mediaRecorder.start();
};

stopBtn.onclick = async () => {
    mediaRecorder.stop();
    mediaRecorder.onstop = () => {
        const blob = new Blob(audioChunks, { type: 'audio/wav' });
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = () => {
            const base64data = reader.result;
            // Send to Streamlit directly using st.session_state hack
            fetch(window.location.href, {
                method: "POST",
                body: JSON.stringify({audio: base64data}),
                headers: {"Content-Type": "application/json"}
            });
        };
    };
};
</script>
""", height=100, scrolling=False)

# --- RECEIVE AUTOMATIC AUDIO IN PYTHON ---
import json

def handle_audio():
    if st.experimental_get_query_params():
        params = st.experimental_get_query_params()
        audio_base64 = params.get("audio", [""])[0]
        if audio_base64:
            audio_bytes = base64.b64decode(audio_base64.split(",")[1])
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

# This is a placeholder since Streamlit Cloud cannot receive POST via JS fetch.
# In production, you would use a Streamlit component that allows two-way communication.
# For now, the Base64 manual input remains the fallback.
audio_base64 = st.text_input("Paste Base64 audio here after recording", "")
if audio_base64:
    audio_bytes = base64.b64decode(audio_base64.split(",")[1])
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

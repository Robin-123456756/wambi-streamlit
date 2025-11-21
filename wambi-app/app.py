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

# --- PINK THEME STYLING ---
st.markdown("""
<style>
body { background-color: #fff0f5; }
h1,h2,h3 { color: #ff1493; }
button.record-btn {
    background-color: #ff69b4;
    color: white;
    font-size: 16px;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    margin-right: 10px;
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

# --- START MY DAY ---
if st.button("Start My Day", key="start_day"):
    st.success("✅ Wambi Activated")

    # Greeting Audio
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    # Simulated Vitals Card
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

# --- LIVE MIC RECORDING ---
st.subheader("🎤 Speak to Wambi (Live Browser Mic)")

components.html("""
<div>
  <button class="record-btn" id="startBtn">Start Recording</button>
  <button class="record-btn" id="stopBtn">Stop Recording</button>
</div>
<script>
let startBtn = document.getElementById('startBtn');
let stopBtn = document.getElementById('stopBtn');
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
      const el = document.getElementById("st_audio");
      el.value = base64data;
      el.dispatchEvent(new Event('change'));
    };
  };
};
</script>
<input type="hidden" id="st_audio" name="st_audio">
""", height=120)

# --- Hidden input to receive audio from JS ---
audio_base64 = st.text_input("Hidden Audio Input", "", key="st_audio")

# --- Auto transcription ---
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

st.markdown("---")

# --- VOICE COMMAND UPLOADER (backup) ---
st.subheader("🎙️ Upload Voice Command")
uploaded_file = st.file_uploader("Upload a .wav audio file (Max: 10MB)", type=["wav"], key="voice_upload")
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
st.caption("Powered by Streamlit | Wambi AI (Premium Preview)")

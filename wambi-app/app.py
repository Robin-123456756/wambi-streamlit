import streamlit as st
from gtts import gTTS
import random
import speech_recognition as sr
import tempfile
from datetime import datetime
from streamlit_audio_recorder import audio_recorder
import base64
import io
import numpy as np
from scipy.io.wavfile import write

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
        "High

import streamlit as st
from gtts import gTTS
import os
import random
import speech_recognition as sr

# 🔧 THIS MUST BE FIRST
st.set_page_config(page_title="Wambi AI", page_icon="🌞")

st.title("🌞 Good Morning, Hard Guy")

# Function for voice input
def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening... Say something.")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("❌ Wambi couldn’t understand you.")
        except sr.RequestError:
            st.error("⚠️ Could not reach Google Speech API.")

if st.button("Start My Day"):
    st.success("✅ Wambi Activated")

    # Alarm greeting
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])

    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")

    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")

    st.subheader("🏋️‍♂️ Exercise Tip")
    tip = random.choice([
        "20-minute morning walk",
        "15-minute yoga stretch",
        "10 push-ups, 20 squats",
        "High-Intensity 5-minute HIIT"
    ])
    st.write(f"Today’s suggestion: **{tip}**")

    # Personalized message
    farewell = f"All set, Hard Guy. Crush the day."
    tts = gTTS(farewell)
    tts.save("farewell.mp3")
    st.audio("farewell.mp3", format="audio/mp3")

# Voice interaction button
if st.button("🎙️ Talk to Wambi"):
    command = listen_to_user()
    if command:
        if "coffee" in command.lower():
            st.write("☕ I’ll get your coffee preferences ready.")
        elif "exercise" in command.lower():
            st.write("💪 Time for some fitness.")
        else:
            st.write("🤖 I heard you, but I’m still learning that command.")


# ✅ THIS MUST BE ABSOLUTELY FIRST
st.set_page_config(page_title="Wambi AI", page_icon="🌞")

from gtts import gTTS
import os
import random

st.title("🌞 Good Morning, Hard Guy")

if st.button("Start My Day"):
    st.success("✅ Wambi Activated")

    # Alarm greeting
    phrase = "Wambi, remember the words of your Father."
    tts = gTTS(phrase)
    tts.save("alarm.mp3")
    st.audio("alarm.mp3", format="audio/mp3")

    st.subheader("🩺 Vital Sign Check (Simulated)")
    heart_rate = random.randint(65, 85)
    oxygen = random.randint(96, 99)
    stress_level = random.choice(["Low", "Normal", "Elevated"])

    st.write(f"Heart Rate: **{heart_rate} bpm**")
    st.write(f"Oxygen Level: **{oxygen}%**")
    st.write(f"Stress Level: **{stress_level}**")

    st.subheader("☕ Coffee Sugar Recommendation")
    sugar = round(0.03 * heart_rate, 1)
    st.write(f"Recommended sugar for your coffee: **{sugar} grams**")

    st.subheader("🏋️‍♂️ Exercise Tip")
    tip = random.choice([
        "20-minute morning walk",
        "15-minute yoga stretch",
        "10 push-ups, 20 squats",
        "High-Intensity 5-minute HIIT"
    ])
    st.write(f"Today’s suggestion: **{tip}**")

    # Personalized message
    farewell = f"All set, Hard Guy. Crush the day."
    tts = gTTS(farewell)
    tts.save("farewell.mp3")
    st.audio("farewell.mp3", format="audio/mp3")


import streamlit as st
from gtts import gTTS

st.title("🎙️ Wambi Voice Test")

# Voice message
message = "Hard Guy, Wambi is ready to serve you."

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


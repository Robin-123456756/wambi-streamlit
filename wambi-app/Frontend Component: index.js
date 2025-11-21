import React, { useState } from "react"
import { withStreamlitConnection, Streamlit } from "streamlit-component-lib"

const LiveMic = () => {
    const [mediaRecorder, setMediaRecorder] = useState(null)
    const [audioChunks, setAudioChunks] = useState([])

    const startRecording = async () => {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
        const recorder = new MediaRecorder(stream)
        recorder.ondataavailable = e => setAudioChunks(prev => [...prev, e.data])
        recorder.start()
        setMediaRecorder(recorder)
    }

    const stopRecording = () => {
        mediaRecorder.stop()
        mediaRecorder.onstop = () => {
            const blob = new Blob(audioChunks, { type: "audio/wav" })
            const reader = new FileReader()
            reader.readAsArrayBuffer(blob)
            reader.onloadend = () => {
                Streamlit.setComponentValue(reader.result)
            }
        }
    }

    return (
        <div>
            <button onClick={startRecording}>Start Recording</button>
            <button onClick={stopRecording}>Stop Recording</button>
        </div>
    )
}

export default withStreamlitConnection(LiveMic)

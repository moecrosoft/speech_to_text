# 🎧 Speech-to-Text Transcription AI

An end-to-end AI application that allows users to record their voice and get real-time transcriptions. This project combines deep learning (Wav2Vec2), a FastAPI backend, a Streamlit frontend, a PostgreSQL database, and full Dockerized deployment.

---

## 📌 Overview

Users can:
- Record audio directly from the browser
- Get an AI transcription of their speech
- View transcription history stored in the database

---

## 🧠 How It Works

1. **Record** — User records audio from the Streamlit UI
2. **Upload** — Frontend sends the audio file to the backend via `POST /transcribe`
3. **Transcribe** — Backend loads the `.wav` file, runs it through the **Wav2Vec2** model (Hugging Face), and converts the waveform to text
4. **Store** — Transcription is saved to PostgreSQL
5. **Display** — Transcribed text is returned and shown in the UI
6. **History** — Past transcriptions are retrieved via `GET /history`

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI, Hugging Face Transformers, PyTorch, psycopg2 |
| Frontend | Streamlit |
| Database | PostgreSQL |
| DevOps | Docker, Docker Compose, AWS EC2, GitHub Actions |

---

## 📂 Project Structure
```
speech_to_text/
│
├── backend/
│   ├── main.py
│   ├── model.py
│   ├── db.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

---

## 🚀 Getting Started
```bash
git clone https://github.com/moecrosoft/speech_to_text.git
cd speech_to_text
docker-compose up -d --build
```

This starts:
- **Frontend** → http://localhost:8501
- **Backend** → http://localhost:8000
- **PostgreSQL** database

---

## 🔗 API Reference

### `POST /transcribe`

**Request:**
```json
{ "file": "audio.wav" }
```

**Response:**
```json
{ "text": "hello world" }
```

### `GET /history`

**Response:**
```json
["hello world", "this is a test transcription"]
```

---

## 📊 Model Details

| Property | Value |
|---|---|
| Model | `facebook/wav2vec2-base-960h` |
| Input | 16kHz audio waveform |
| Output | Transcribed text |
| Framework | PyTorch |
| Processor | Wav2Vec2Processor |
| Decoding | Greedy decoding (`torch.argmax`) |

---

## 🎯 Features

- ✅ Real-time speech-to-text transcription
- ✅ Audio recording in the browser
- ✅ Transcription history tracking
- ✅ Fully Dockerized deployment
- ✅ One-command startup
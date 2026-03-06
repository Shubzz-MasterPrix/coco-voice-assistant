# Coco - AI Voice Assistant

A Python voice assistant powered by Google Gemini AI. Say "Hey Coco" and ask anything.

## Quick Start

1. **Clone & setup:**

```bash
   git clone https://github.com/yourusername/coco-voice-assistant.git
   cd coco-voice-assistant
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```

2. **Add API key:**
   - Get free key: https://aistudio.google.com/app/apikey
   - Create `.env` file: `GEMINI_API_KEY=your_key_here`

3. **Run:**

```bash
   python main.py
```

## Commands

- "Hey Coco" → activates assistant
- "Open YouTube/Google" → opens websites
- Any question → AI answers
- "Goodbye" → exits

## Tech Stack

Python • Google Gemini • SpeechRecognition • pyttsx3

---

**Troubleshooting:** If PyAudio fails on Windows: `pip install pipwin` then `pipwin install pyaudio`

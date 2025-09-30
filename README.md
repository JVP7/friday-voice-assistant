```bash
# Friday – Voice Assistant

A personal assistant built with LiveKit Agents, inspired by Iron Man’s AI.
Friday handles STT → LLM → TTS, can search the web, check weather, and send emails.

## Features
- 🎙️ Speech-to-Text (Deepgram or Google STT)
- 💬 LLM responses (Google Gemini)
- �� Text-to-Speech (Cartesia)
- 🌦️ Weather via `wttr.in`
- 🔍 Web search (DuckDuckGo via LangChain + ddgs)
- 📧 Email sending (Gmail App Password)

## Requirements
- Python 3.10+
- API credentials for enabled services:
  - DEEPGRAM_API_KEY (if using Deepgram STT) or Google Cloud creds (if using Google STT)
  - GOOGLE_API_KEY (Gemini)
  - CARTESIA_API_KEY (TTS)
  - GMAIL_USER + GMAIL_APP_PASSWORD (App Password, not your normal password)

## Setup
git clone <your-repo-url>
cd <your-repo>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Environment Variables (.env)
GMAIL_USER=youraddress@gmail.com
GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
DEEPGRAM_API_KEY=your_deepgram_key    # or set Google STT ADC instead
GOOGLE_API_KEY=your_gemini_key
CARTESIA_API_KEY=your_cartesia_key

## Run (Console)
python agent.py console

## Run (Dev / Playground)
python agent.py dev

## Future Upgrades
1 - Add a feature that will make it remember things
2 - Play music
3 - Long-term conversations

```

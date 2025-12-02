# 🎤 English Training Voice Assistant (Local)

AI-powered voice assistant for English conversation practice - 100% offline and private.

## ✨ Features

- 🗣️ **Voice conversation** in English
- 🎯 **Real-time corrections** (grammar, vocabulary, pronunciation)
- 🔊 **AI speaks back** (listening practice)
- 📝 **Conversation history** with feedback
- 🔒 **100% offline** - no data sent to cloud
- 💰 **Free** - no API costs

## 🛠️ Tech Stack

- **STT (Speech-to-Text):** Whisper (faster-whisper)
- **LLM (Conversation):** Ollama + LLaMA 3
- **TTS (Text-to-Speech):** Google TTS (natural voice) ⭐ → Piper → espeak (fallback)
- **Backend:** Python 3.10+
- **Interface:** Terminal + Web UI (optional)

## 📋 Prerequisites

- Python 3.10+
- 8GB+ RAM recommended
- GPU optional (NVIDIA CUDA for faster processing)
- Microphone

## 🚀 Quick Start

### 1. Install dependencies

```bash
# Install Python dependencies
source venv/bin/activate
pip install -r requirements.txt

# Install Ollama (LLM runtime)
curl -fsSL https://ollama.com/install.sh | sh

# Pull LLaMA 3 model
ollama pull llama3

# OPTIONAL: Install better voice quality (HIGHLY RECOMMENDED!)
sudo apt-get install -y ffmpeg mpg123
pip install gtts
```

### 2. Run the assistant

```bash
source venv/bin/activate
python main.py
```

### 3. Start talking in English!

The assistant will:
1. Listen to your voice
2. Transcribe what you said
3. Respond with corrections and conversation
4. Speak the response back to you

## 📁 Project Structure

```
LLMLOCAL/
├── main.py              # Main application
├── modules/
│   ├── stt.py          # Speech-to-Text (Whisper)
│   ├── llm.py          # LLM conversation (Ollama)
│   ├── tts.py          # Text-to-Speech (Piper)
│   └── corrections.py  # Grammar/pronunciation feedback
├── prompts/
│   └── teacher.txt     # System prompt for English teacher
├── config/
│   └── settings.yaml   # Configuration
├── history/            # Conversation logs
└── requirements.txt    # Python dependencies
```

## ⚙️ Configuration

Edit `config/settings.yaml` to customize:

- Conversation topics
- English level (beginner/intermediate/advanced)
- Correction intensity
- Voice settings
- LLM model

## 🎯 Usage Examples

**Casual conversation:**
```
You: "Hey, how are you today?"
AI: "I'm doing great, thanks for asking! How about you?
     By the way, your pronunciation was excellent!"
```

**With corrections:**
```
You: "Yesterday I go to the park"
AI: "I understand! Just a small correction: 'Yesterday I *went* to the park'
     (past tense). Now, what did you do there?"
```

## 🤝 Contributing

Feel free to open issues or submit PRs!

## 📄 License

MIT

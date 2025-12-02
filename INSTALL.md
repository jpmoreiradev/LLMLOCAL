# 📦 Installation Guide

Complete guide to set up your English Training Voice Assistant.

## Prerequisites

- **OS:** Linux, macOS, or WSL2 (Windows)
- **Python:** 3.10 or higher
- **RAM:** 8GB minimum (16GB recommended)
- **Storage:** 10GB free space (for models)
- **Microphone:** Any working microphone
- **GPU (optional):** NVIDIA GPU with CUDA for faster processing

## Quick Install (Recommended)

```bash
# Run the automated setup script
./setup.sh
```

This will:
- Create a virtual environment
- Install all Python dependencies
- Install Ollama (LLM runtime)
- Download the LLaMA 3 model
- Install audio dependencies

## Manual Installation

If you prefer to install manually or the automated script fails:

### 1. Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Install Ollama (LLM)

**Linux/macOS:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download from [ollama.com](https://ollama.com/download)

**Download the model:**
```bash
ollama pull llama3
```

### 3. Audio Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio espeak
```

**macOS:**
```bash
brew install portaudio
```

**Windows:**
```bash
# PyAudio wheels available via pip
pip install pipwin
pipwin install pyaudio
```

### 4. Whisper (STT)

Already included in requirements.txt, but if you want GPU acceleration:

```bash
# Install CUDA-enabled PyTorch first
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 5. Text-to-Speech (Optional)

**Option 1: Use system TTS (espeak/say)**
- Already works out of the box
- Lower quality but simple

**Option 2: Install Piper (better quality)**
```bash
# Download Piper
wget https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz
tar -xzf piper_amd64.tar.gz
sudo mv piper /usr/local/bin/

# Download voice model
mkdir -p models/tts
cd models/tts
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx
wget https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json
```

## Verify Installation

```bash
# Check Python packages
pip list | grep -E "whisper|ollama|sounddevice"

# Check Ollama
ollama list

# Check audio
python -c "import sounddevice; print(sounddevice.query_devices())"
```

## Troubleshooting

### Microphone not detected

```bash
# List audio devices
python -c "import sounddevice; print(sounddevice.query_devices())"

# Test recording
python -c "import sounddevice as sd; import numpy as np; print('Recording...'); sd.rec(int(3 * 16000), samplerate=16000, channels=1); sd.wait(); print('Done')"
```

### Ollama connection error

```bash
# Start Ollama service
ollama serve

# In another terminal, test it
ollama run llama3 "Hello"
```

### PortAudio errors

**Linux:**
```bash
sudo apt-get install libasound2-dev
```

**macOS:**
```bash
brew reinstall portaudio
```

### GPU not being used

Edit [config/settings.yaml](config/settings.yaml):
```yaml
stt:
  device: "cuda"  # Change from "cpu" to "cuda"
```

## Performance Optimization

### Use smaller Whisper model for faster STT

Edit [config/settings.yaml](config/settings.yaml):
```yaml
stt:
  model: "tiny"  # Fastest (but less accurate)
  # Options: tiny, base, small, medium, large
```

### Use smaller LLM model

```bash
# Instead of llama3 (8B params), use a smaller model
ollama pull phi3:mini  # 3.8B params - faster

# Or use Mistral
ollama pull mistral
```

Update [config/settings.yaml](config/settings.yaml):
```yaml
llm:
  model: "phi3:mini"
```

### Enable GPU acceleration

Make sure you have CUDA installed:
```bash
nvidia-smi  # Check GPU

# Install CUDA-enabled packages
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Next Steps

Once installed:

1. Run the assistant: `python main.py`
2. Customize settings: edit [config/settings.yaml](config/settings.yaml)
3. Start practicing English!

## Getting Help

- **Ollama docs:** https://ollama.com/docs
- **Whisper docs:** https://github.com/openai/whisper
- **Report issues:** Open an issue on GitHub

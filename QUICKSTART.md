# 🚀 Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Install System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-pyaudio libasound2-dev espeak
```

**Arch Linux:**
```bash
sudo pacman -S portaudio espeak
```

**macOS:**
```bash
brew install portaudio espeak
```

## Step 2: Install Ollama (LLM)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
```

## Step 3: Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install --upgrade pip
pip install -r requirements.txt
```

## Step 4: Run!

```bash
python main.py
```

## Troubleshooting

### PyAudio Error?

If you get "portaudio.h not found":

```bash
# Install PortAudio first
sudo apt-get install portaudio19-dev

# Then reinstall
pip install pyaudio
```

### Ollama not found?

```bash
# Make sure Ollama is running
ollama serve &

# Test it
ollama run llama3 "hello"
```

### No microphone detected?

```bash
# List audio devices
python3 -c "import sounddevice; print(sounddevice.query_devices())"
```

## Minimal Installation (No Voice)

If you just want to test without audio:

1. Edit [config/settings.yaml](config/settings.yaml):
```yaml
tts:
  enabled: false  # Disable voice output
```

2. Use text mode:
```bash
python main.py --text-mode  # Coming soon!
```

## What's Next?

- Read [USAGE.md](USAGE.md) for tips on practicing
- Customize [config/settings.yaml](config/settings.yaml)
- Start talking in English!

## Need Help?

Check [INSTALL.md](INSTALL.md) for detailed installation instructions.

#!/bin/bash
# Setup script for English Training Voice Assistant

set -e

echo "🚀 Setting up English Training Voice Assistant..."
echo ""

# Check Python version
echo "📋 Checking Python version..."
python3 --version || { echo "❌ Python 3 not found. Please install Python 3.10+"; exit 1; }

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Ollama
echo "🤖 Installing Ollama..."
if ! command -v ollama &> /dev/null; then
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama already installed"
fi

# Pull LLaMA 3 model
echo "📥 Downloading LLaMA 3 model (this may take a few minutes)..."
ollama pull llama3

# Install system dependencies for audio
echo "🔊 Installing audio dependencies..."
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux. Installing portaudio..."
    sudo apt-get update
    sudo apt-get install -y portaudio19-dev python3-pyaudio espeak
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS. Installing portaudio..."
    brew install portaudio
fi

# Install Piper TTS (optional)
echo "🗣️ Installing Piper TTS (optional - using espeak as fallback)..."
# Piper installation is optional - the system will use espeak if available

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p temp_audio history logs models

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the assistant:"
echo "  1. Activate virtual environment: source venv/bin/activate"
echo "  2. Run: python main.py"
echo ""
echo "📖 Check README.md for more information"

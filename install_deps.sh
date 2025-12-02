#!/bin/bash
# Install system dependencies for English Training Voice Assistant

echo "🔧 Installing system dependencies..."

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "📦 Detected Linux"

    # Detect package manager
    if command -v apt-get &> /dev/null; then
        echo "Using apt-get..."
        sudo apt-get update
        sudo apt-get install -y \
            portaudio19-dev \
            python3-pyaudio \
            libasound2-dev \
            espeak \
            ffmpeg

    elif command -v pacman &> /dev/null; then
        echo "Using pacman..."
        sudo pacman -Sy --noconfirm \
            portaudio \
            espeak \
            ffmpeg

    elif command -v dnf &> /dev/null; then
        echo "Using dnf..."
        sudo dnf install -y \
            portaudio-devel \
            espeak \
            ffmpeg
    else
        echo "❌ Unknown package manager. Please install manually:"
        echo "  - portaudio19-dev"
        echo "  - espeak"
        echo "  - ffmpeg"
        exit 1
    fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "📦 Detected macOS"

    if ! command -v brew &> /dev/null; then
        echo "❌ Homebrew not found. Please install from https://brew.sh"
        exit 1
    fi

    brew install portaudio espeak ffmpeg

else
    echo "❌ Unsupported OS: $OSTYPE"
    exit 1
fi

echo "✅ System dependencies installed!"
echo ""
echo "Next steps:"
echo "  1. source venv/bin/activate"
echo "  2. pip install -r requirements.txt"
echo "  3. pip install pyaudio  # Now it should work!"

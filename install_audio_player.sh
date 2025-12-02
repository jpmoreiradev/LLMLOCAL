#!/bin/bash
# Install audio player for Google TTS

echo "🔊 Installing audio player for better TTS quality..."

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "📦 Detected Linux"

    if command -v apt-get &> /dev/null; then
        echo "Installing mpg123..."
        sudo apt-get update
        sudo apt-get install -y mpg123
    elif command -v pacman &> /dev/null; then
        echo "Installing mpg123..."
        sudo pacman -Sy --noconfirm mpg123
    elif command -v dnf &> /dev/null; then
        echo "Installing mpg123..."
        sudo dnf install -y mpg123
    fi

elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "📦 Detected macOS"
    brew install mpg123
fi

echo "✅ Audio player installed!"
echo ""
echo "Now you can use Google TTS for much better voice quality!"
echo "Run: python main.py"
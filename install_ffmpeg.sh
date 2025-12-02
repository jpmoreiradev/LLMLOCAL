#!/bin/bash
# Install ffmpeg and audio tools

echo "📦 Installing audio tools (ffmpeg, mpg123)..."

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y ffmpeg mpg123
    elif command -v pacman &> /dev/null; then
        sudo pacman -Sy --noconfirm ffmpeg mpg123
    elif command -v dnf &> /dev/null; then
        sudo dnf install -y ffmpeg mpg123
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install ffmpeg mpg123
fi

echo "✅ Audio tools installed!"
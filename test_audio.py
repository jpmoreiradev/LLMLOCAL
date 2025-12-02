#!/usr/bin/env python3
"""
Test audio recording settings
Use this to test if the microphone is detecting your voice correctly
"""

import numpy as np
import sounddevice as sd
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
import time

console = Console()


def test_microphone_volume():
    """Test microphone and show volume levels in real-time"""
    console.print("\n[bold cyan]🎤 Microphone Volume Test[/bold cyan]")
    console.print("[dim]Speak into your microphone to see the volume level[/dim]")
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    sample_rate = 16000
    duration = 0.1  # Check every 100ms

    volumes = []

    try:
        while True:
            # Record a short snippet
            audio = sd.rec(int(duration * sample_rate),
                          samplerate=sample_rate,
                          channels=1,
                          dtype='float32')
            sd.wait()

            # Calculate volume
            volume = np.abs(audio).mean()
            volumes.append(volume)

            # Keep last 10 readings
            if len(volumes) > 10:
                volumes.pop(0)

            avg_volume = np.mean(volumes)

            # Visual indicator
            bars = int(volume * 1000)  # Scale for visibility
            bar = "█" * min(bars, 50)

            # Color based on level
            if volume > 0.01:
                color = "green"
                status = "LOUD ✅"
            elif volume > 0.005:
                color = "yellow"
                status = "GOOD 👍"
            elif volume > 0.002:
                color = "orange"
                status = "LOW ⚠️"
            else:
                color = "red"
                status = "SILENT 🔇"

            console.print(f"[{color}]{bar:<50}[/{color}] {volume:.5f} - {status}", end="\r")

    except KeyboardInterrupt:
        console.print("\n\n[bold]Summary:[/bold]")
        console.print(f"Average volume: {avg_volume:.5f}")
        console.print(f"Current threshold: 0.005")

        if avg_volume > 0.01:
            console.print("\n[green]✅ Your microphone volume is good![/green]")
        elif avg_volume > 0.005:
            console.print("\n[yellow]⚠️  Volume is a bit low, but should work[/yellow]")
        else:
            console.print("\n[red]❌ Volume is too low[/red]")
            console.print("[yellow]Try:[/yellow]")
            console.print("  1. Speak louder")
            console.print("  2. Move closer to the microphone")
            console.print("  3. Increase system microphone volume")


def test_recording_with_timeout():
    """Test the actual recording function with visual feedback"""
    console.print("\n[bold cyan]🎙️  Recording Test with Auto-Stop[/bold cyan]")
    console.print("[dim]This simulates how the assistant will record your voice[/dim]")
    console.print("[yellow]Start speaking after 'Listening...' appears[/yellow]\n")

    input("Press Enter to start...")

    from modules.stt import SpeechToText

    stt = SpeechToText(model_size="base")

    console.print("\n[bold green]Recording now![/bold green]")
    audio = stt.record_audio(duration=15)

    if len(audio) > 0:
        console.print(f"\n[green]✅ Recorded {len(audio)/16000:.1f} seconds of audio[/green]")

        # Analyze the recording
        volume = np.abs(audio).mean()
        console.print(f"Average volume: {volume:.5f}")

        # Transcribe
        console.print("\n[yellow]Transcribing...[/yellow]")
        text = stt.transcribe(audio)
        console.print(f"\n[bold]You said:[/bold] {text}")

        if not text or len(text.strip()) < 3:
            console.print("\n[red]⚠️  Transcription failed or too short[/red]")
            console.print("[yellow]Tips:[/yellow]")
            console.print("  • Speak more clearly")
            console.print("  • Speak louder")
            console.print("  • Check if microphone is working")
    else:
        console.print("\n[red]❌ No audio recorded![/red]")
        console.print("[yellow]Check if your microphone is working[/yellow]")


def main():
    """Main test menu"""
    console.print("[bold]🧪 Audio Testing Tool[/bold]\n")
    console.print("Choose a test:")
    console.print("  1. Microphone volume test (real-time)")
    console.print("  2. Recording test with transcription")
    console.print("  3. Both tests")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        test_microphone_volume()
    elif choice == "2":
        test_recording_with_timeout()
    elif choice == "3":
        test_microphone_volume()
        console.print("\n" + "="*60 + "\n")
        test_recording_with_timeout()
    else:
        console.print("[red]Invalid choice[/red]")


if __name__ == "__main__":
    main()
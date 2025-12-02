#!/usr/bin/env python3
"""
Test TTS engines to compare voice quality
"""

from modules.tts import GoogleTTS, SimpleTTS
from rich.console import Console

console = Console()

def test_google_tts():
    """Test Google TTS (high quality)"""
    console.print("\n[bold cyan]Testing Google TTS (High Quality)...[/bold cyan]")

    try:
        tts = GoogleTTS()

        if not tts.enabled:
            console.print("[yellow]Google TTS not available[/yellow]")
            return False

        test_text = "Hello! This is the Google Text to Speech engine. The voice quality is much more natural than espeak."

        console.print(f"[green]Speaking:[/green] {test_text}")
        tts.speak(test_text)

        console.print("[green]✅ Google TTS working![/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        return False


def test_espeak():
    """Test espeak (fallback)"""
    console.print("\n[bold cyan]Testing espeak (Fallback)...[/bold cyan]")

    try:
        tts = SimpleTTS()

        if not tts.enabled:
            console.print("[yellow]espeak not available[/yellow]")
            return False

        test_text = "Hello! This is the espeak engine. It sounds more robotic."

        console.print(f"[green]Speaking:[/green] {test_text}")
        tts.speak(test_text)

        console.print("[green]✅ espeak working![/green]")
        return True

    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")
        return False


def main():
    console.print("[bold]🎤 TTS Engine Comparison Test[/bold]\n")

    # Test both engines
    google_works = test_google_tts()
    espeak_works = test_espeak()

    # Summary
    console.print("\n" + "="*50)
    console.print("[bold]Summary:[/bold]\n")

    if google_works:
        console.print("[green]✅ Google TTS: Working (RECOMMENDED - best quality)[/green]")
    else:
        console.print("[yellow]⚠️  Google TTS: Not available[/yellow]")
        console.print("[dim]   Install: pip install gtts[/dim]")
        console.print("[dim]   Install player: sudo apt-get install mpg123[/dim]")

    if espeak_works:
        console.print("[green]✅ espeak: Working (fallback - robotic voice)[/green]")
    else:
        console.print("[red]❌ espeak: Not available[/red]")

    console.print("\nThe assistant will automatically use the best available TTS engine.")


if __name__ == "__main__":
    main()
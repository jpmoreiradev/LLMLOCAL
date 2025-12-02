#!/usr/bin/env python3
"""
Quick test - just record and show what was said
"""

from modules.stt import SpeechToText
from rich.console import Console

console = Console()

console.print("[bold cyan]🎤 Quick Recording Test[/bold cyan]\n")
console.print("[yellow]This will test the new settings:[/yellow]")
console.print("  • 6 seconds of silence before stopping")
console.print("  • Visual feedback while you speak")
console.print("  • More forgiving detection\n")

input("Press Enter to start recording...")

stt = SpeechToText(model_size="base")

console.print("\n[bold green]Start speaking now![/bold green]\n")

audio = stt.record_audio(duration=45)  # 45 second max

if len(audio) > 0:
    duration = len(audio) / 16000
    console.print(f"\n[green]✅ Recorded {duration:.1f} seconds[/green]")

    console.print("\n[yellow]Transcribing...[/yellow]")
    text = stt.transcribe(audio)

    console.print(f"\n[bold]📝 You said:[/bold]")
    console.print(f"[cyan]{text}[/cyan]\n")

    if len(text.strip()) < 3:
        console.print("[red]⚠️  Text too short - speak louder or closer to mic[/red]")
else:
    console.print("\n[red]❌ No audio recorded[/red]")
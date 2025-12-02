#!/usr/bin/env python3
"""
Test MANUAL recording mode - press Enter to stop
"""

from modules.stt import SpeechToText
from rich.console import Console

console = Console()

console.print("[bold cyan]🎤 Manual Recording Mode Test[/bold cyan]\n")
console.print("[yellow]How it works:[/yellow]")
console.print("  1. Press Enter to START recording")
console.print("  2. Speak as much as you want")
console.print("  3. Press Enter again to STOP")
console.print("  4. NO automatic stopping!\n")

console.print("[green]This is PERFECT for long speeches or when you need pauses![/green]\n")

input("Press Enter to begin...")

stt = SpeechToText(model_size="base")

console.print("\n")

# Test manual recording
text = stt.listen_and_transcribe_manual(max_duration=120)  # 2 minutes max

if text and len(text.strip()) >= 3:
    console.print(f"\n[bold]📝 You said:[/bold]")
    console.print(f"[cyan]{text}[/cyan]\n")

    word_count = len(text.split())
    console.print(f"[green]✅ Transcribed {word_count} words successfully![/green]")
else:
    console.print("\n[red]⚠️  No text transcribed - speak louder or check microphone[/red]")
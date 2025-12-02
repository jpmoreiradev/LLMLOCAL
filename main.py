#!/usr/bin/env python3
"""
English Training Voice Assistant
Main application - Talk with AI to practice English
"""

import yaml
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from datetime import datetime
import json

from modules.stt import SpeechToText
from modules.llm import EnglishTeacher
from modules.tts import TextToSpeech, SimpleTTS, GoogleTTS


console = Console()


class EnglishAssistant:
    def __init__(self, config_path="config/settings.yaml"):
        """Initialize the English training assistant"""

        # Load configuration
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

        # Initialize modules
        console.print("[yellow]Loading AI modules...[/yellow]")

        # Speech-to-Text
        stt_config = self.config['stt']
        self.stt = SpeechToText(
            model_size=stt_config['model'],
            device=stt_config['device'],
            language=stt_config['language']
        )

        # LLM Teacher
        llm_config = self.config['llm']
        self.teacher = EnglishTeacher(
            model=llm_config['model'],
            temperature=llm_config['temperature']
        )

        # Text-to-Speech (Priority: GoogleTTS > Piper > SimpleTTS)
        tts_config = self.config['tts']
        tts_initialized = False

        # Try GoogleTTS first (best quality)
        try:
            self.tts = GoogleTTS(lang='en', slow=False)
            if self.tts.enabled:
                tts_initialized = True
        except Exception as e:
            console.print(f"[dim]GoogleTTS not available: {e}[/dim]")

        # Try Piper if GoogleTTS failed
        if not tts_initialized:
            try:
                self.tts = TextToSpeech(
                    voice=tts_config['voice'],
                    speed=tts_config['speed']
                )
                if self.tts.enabled:
                    tts_initialized = True
            except Exception as e:
                console.print(f"[dim]Piper not available: {e}[/dim]")

        # Fallback to SimpleTTS (espeak)
        if not tts_initialized:
            console.print("[yellow]Using espeak fallback (basic quality)[/yellow]")
            self.tts = SimpleTTS()

        if hasattr(self.tts, 'set_enabled'):
            self.tts.set_enabled(tts_config['enabled'])

        # Session data
        self.session_start = datetime.now()
        self.conversation_log = []

        console.print("[green]✅ All systems ready![/green]\n")

    def display_welcome(self):
        """Show welcome message"""
        welcome = f"""
[bold cyan]🎓 English Training Voice Assistant[/bold cyan]

[green]Ready to practice English![/green]

Student level: [yellow]{self.config['student']['level']}[/yellow]
Focus: [yellow]{', '.join(self.config['student']['focus_areas'])}[/yellow]

[dim]Tips:
• Speak clearly in English
• The AI will correct your mistakes gently
• Press Ctrl+C to stop
• Type 'summary' to review your session[/dim]
        """
        console.print(Panel(welcome, border_style="cyan"))

    def save_session(self):
        """Save conversation history"""
        if not self.config['history']['save_conversations']:
            return

        history_dir = Path("history")
        history_dir.mkdir(exist_ok=True)

        session_file = history_dir / f"session_{self.session_start.strftime('%Y%m%d_%H%M%S')}.json"

        session_data = {
            "start_time": self.session_start.isoformat(),
            "end_time": datetime.now().isoformat(),
            "student_level": self.config['student']['level'],
            "conversation": self.conversation_log
        }

        with open(session_file, 'w') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)

        console.print(f"[dim]💾 Session saved to {session_file}[/dim]")

    def run(self):
        """Main conversation loop"""
        self.display_welcome()

        # Initial greeting in Portuguese
        greeting = "Olá! Sou a Sarah, sua professora de inglês. Vamos praticar! Pode falar em " \
        "português ou inglês, como preferir."
        console.print(f"\n[blue]🤖 Teacher:[/blue] {greeting}\n")
        self.tts.speak(greeting)

        try:
            while True:
                # Check recording mode
                recording_mode = self.config['audio'].get('recording_mode', 'auto')

                if recording_mode == 'manual':
                    # MANUAL MODE: Always listening, press Enter to stop
                    student_text = self.stt.listen_and_transcribe_manual(
                        max_duration=self.config['audio']['max_recording_time']
                    )
                else:
                    # AUTO MODE: Automatic silence detection
                    input()  # Wait for Enter

                    student_text = self.stt.listen_and_transcribe(
                        duration=self.config['audio']['max_recording_time']
                    )

                if not student_text or len(student_text.strip()) < 3:
                    console.print("[yellow]⚠️  I didn't catch that. Please try again.[/yellow]\n")
                    continue

                console.print(f"\n[green]👤 You:[/green] {student_text}\n")

                # Check for commands
                if student_text.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    farewell = "Goodbye! Great practice today. Keep up the good work!"
                    console.print(f"[blue]🤖 Teacher:[/blue] {farewell}\n")
                    self.tts.speak(farewell)
                    break

                if student_text.lower() == 'summary':
                    summary = self.teacher.get_conversation_summary()
                    console.print(Panel(summary, title="📊 Session Summary", border_style="blue"))
                    continue

                # Get teacher response
                teacher_response = self.teacher.chat(student_text)
                console.print(f"[blue]🤖 Teacher:[/blue] {teacher_response}\n")

                # Speak response
                self.tts.speak(teacher_response)

                # Log conversation
                self.conversation_log.append({
                    "timestamp": datetime.now().isoformat(),
                    "student": student_text,
                    "teacher": teacher_response
                })

        except KeyboardInterrupt:
            console.print("\n\n[yellow]Session interrupted[/yellow]")

        finally:
            # Session summary
            console.print("\n" + "="*50)
            summary = self.teacher.get_conversation_summary()
            console.print(Panel(summary, title="📊 Session Summary", border_style="green"))

            # Save session
            self.save_session()

            console.print("\n[cyan]Thanks for practicing! See you next time! 👋[/cyan]\n")


def main():
    """Entry point"""
    try:
        assistant = EnglishAssistant()
        assistant.run()
    except FileNotFoundError as e:
        console.print(f"[red]Error: {e}[/red]")
        console.print("[yellow]Make sure config/settings.yaml exists[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise


if __name__ == "__main__":
    main()
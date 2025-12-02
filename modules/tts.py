"""
Text-to-Speech module using multiple engines
Makes the AI speak responses with natural voice
"""

import subprocess
import os
from pathlib import Path
import sounddevice as sd
import soundfile as sf
import tempfile


class TextToSpeech:
    def __init__(self, voice="en_US-lessac-medium", speed=1.0):
        """
        Initialize TTS with Piper

        Args:
            voice: Voice model to use
            speed: Speech speed multiplier
        """
        self.voice = voice
        self.speed = speed
        self.enabled = True

        # Check if piper is installed
        try:
            subprocess.run(["piper", "--version"],
                         capture_output=True, check=True)
            print(f"✅ TTS ready (voice: {voice})")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("⚠️  Piper not found. TTS will use fallback.")
            self.enabled = False

    def speak(self, text):
        """
        Convert text to speech and play it

        Args:
            text: Text to speak
        """
        if not self.enabled:
            print(f"🔊 [Would say: {text}]")
            return

        try:
            # Create temp directory
            temp_dir = Path("temp_audio")
            temp_dir.mkdir(exist_ok=True)
            output_file = temp_dir / "response.wav"

            # Generate speech with piper
            process = subprocess.Popen(
                ["piper", "--model", self.voice, "--output_file", str(output_file)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            process.communicate(input=text.encode())

            # Play audio
            if output_file.exists():
                data, samplerate = sf.read(output_file)
                sd.play(data, samplerate * self.speed)
                sd.wait()
                output_file.unlink()  # Cleanup
            else:
                print("⚠️  Failed to generate speech")

        except Exception as e:
            print(f"⚠️  TTS error: {e}")
            print(f"📝 Text: {text}")

    def speak_async(self, text):
        """
        Speak without blocking (background)

        Args:
            text: Text to speak
        """
        import threading
        thread = threading.Thread(target=self.speak, args=(text,))
        thread.start()

    def set_enabled(self, enabled):
        """Enable or disable TTS"""
        self.enabled = enabled


class SimpleTTS:
    """
    Fallback TTS using system commands (espeak/say)
    """
    def __init__(self):
        self.enabled = True

        # Check available TTS
        if os.system("which espeak > /dev/null 2>&1") == 0:
            self.command = "espeak"
            print("✅ TTS ready (using espeak)")
        elif os.system("which say > /dev/null 2>&1") == 0:
            self.command = "say"
            print("✅ TTS ready (using macOS say)")
        else:
            self.command = None
            print("⚠️  No TTS available")

    def speak(self, text):
        """Speak using system TTS"""
        if not self.enabled or not self.command:
            print(f"🔊 [Would say: {text}]")
            return

        try:
            # Clean text to avoid command injection and quote issues
            clean_text = text.replace('"', '\\"').replace("'", "\\'")

            if self.command == "espeak":
                # Use espeak-ng if available (better quality)
                if os.system("which espeak-ng > /dev/null 2>&1") == 0:
                    # espeak-ng with better settings for more natural voice
                    os.system(f'espeak-ng -v en-us -s 160 -p 50 "{clean_text}" 2>/dev/null')
                else:
                    # Regular espeak with improved settings
                    os.system(f'espeak -v en-us+f3 -s 160 -p 50 "{clean_text}" 2>/dev/null')
            elif self.command == "say":
                os.system(f'say "{clean_text}"')
        except Exception as e:
            print(f"⚠️  TTS error: {e}")
            print(f"📝 Text: {text}")

    def set_enabled(self, enabled):
        """Enable or disable TTS"""
        self.enabled = enabled


class GoogleTTS:
    """
    High-quality TTS using Google Text-to-Speech (gTTS)
    Much more natural voice than espeak
    Supports bilingual (Portuguese + English)
    """
    def __init__(self, lang='en', slow=False):
        self.enabled = True
        self.lang = lang
        self.slow = slow

        try:
            from gtts import gTTS
            self.gTTS = gTTS
            print("✅ TTS ready (using Google TTS - bilingual PT/EN)")
        except ImportError:
            print("⚠️  gTTS not installed. Install with: pip install gtts")
            self.enabled = False
            self.gTTS = None

    def _detect_language_simple(self, text):
        """
        Simple language detection - Portuguese or English
        """
        # Common Portuguese words
        pt_words = ['você', 'está', 'como', 'muito', 'bem', 'tenta', 'diz',
                    'fala', 'seu', 'sua', 'agora', 'boa', 'quase', 'não',
                    'ótimo', 'correto', 'forma', 'de', 'para', 'com', 'que']

        text_lower = text.lower()

        # Count Portuguese words
        pt_count = sum(1 for word in pt_words if f' {word} ' in f' {text_lower} ')

        # If has Portuguese words, speak in Portuguese
        return 'pt' if pt_count >= 1 else 'en'

    def speak(self, text):
        """Convert text to speech using Google TTS with auto language detection"""
        if not self.enabled or not self.gTTS:
            print(f"🔊 [Would say: {text}]")
            return

        try:
            # Detect language
            lang = self._detect_language_simple(text)

            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name

            # Generate speech
            tts = self.gTTS(text=text, lang=lang, slow=self.slow)
            tts.save(temp_file)

            # Play audio
            if os.system("which mpg123 > /dev/null 2>&1") == 0:
                os.system(f"mpg123 -q {temp_file}")
            elif os.system("which ffplay > /dev/null 2>&1") == 0:
                os.system(f"ffplay -nodisp -autoexit -loglevel quiet {temp_file}")
            elif os.system("which mpv > /dev/null 2>&1") == 0:
                os.system(f"mpv --really-quiet {temp_file}")
            else:
                print("⚠️  No audio player found. Install mpg123, ffplay, or mpv")
                print(f"📝 Text: {text}")

            # Cleanup
            try:
                os.unlink(temp_file)
            except:
                pass

        except Exception as e:
            print(f"⚠️  TTS error: {e}")
            print(f"📝 Text: {text}")

    def set_enabled(self, enabled):
        """Enable or disable TTS"""
        self.enabled = enabled


if __name__ == "__main__":
    # Test TTS
    print("\n" + "="*50)
    print("Testing Text-to-Speech")
    print("="*50 + "\n")

    tts = TextToSpeech()

    test_texts = [
        "Hello! I'm your English teacher.",
        "Let's practice some English conversation together.",
        "Great job! Your pronunciation is improving."
    ]

    for text in test_texts:
        print(f"🔊 Speaking: {text}")
        tts.speak(text)
        print()

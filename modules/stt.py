"""
Speech-to-Text module using Whisper
Transcribes user's spoken English to text
"""

import os
import numpy as np
import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel
from pathlib import Path


class SpeechToText:
    def __init__(self, model_size="base", device="cpu", language="en"):
        """
        Initialize Whisper STT

        Args:
            model_size: tiny, base, small, medium, large
            device: cpu or cuda
            language: en for English
        """
        print(f"Loading Whisper model ({model_size})...")
        self.model = WhisperModel(model_size, device=device, compute_type="int8")
        self.language = language
        self.sample_rate = 16000

    def record_audio(self, duration=10, silence_threshold=0.003, max_silence=6.0):
        """
        Record audio from microphone

        Args:
            duration: Maximum recording time in seconds
            silence_threshold: Volume threshold to detect silence (lower = more sensitive)
            max_silence: Stop recording after this many seconds of silence

        Returns:
            numpy array with audio data
        """
        print("🎤 Listening... (will stop after 6 seconds of silence)")
        print("💡 Take your time! Speak naturally and pause as needed")

        recording = []
        silence_counter = 0
        has_speech = False  # Track if we've detected any speech
        last_volume_print = 0
        silence_samples = int(max_silence * self.sample_rate)

        def callback(indata, frames, time, status):
            nonlocal silence_counter, has_speech, last_volume_print
            recording.append(indata.copy())

            # Detect silence
            volume = np.abs(indata).mean()

            # Track if we've heard any speech (more lenient threshold)
            if volume > silence_threshold * 3:  # Increased multiplier for speech detection
                has_speech = True
                silence_counter = 0
                # Visual feedback every 0.5s
                if len(recording) - last_volume_print > self.sample_rate // 4:
                    print("🗣️", end=" ", flush=True)
                    last_volume_print = len(recording)
            elif volume < silence_threshold:
                # Only count silence if we've already detected speech
                if has_speech:
                    silence_counter += frames
                    # Show silence progress every second
                    if silence_counter % self.sample_rate < frames:
                        seconds_silent = silence_counter / self.sample_rate
                        print(f"\n⏱️  Silent for {seconds_silent:.0f}s (will stop at 6s)", end="", flush=True)
            else:
                # In between - be more forgiving, don't reset immediately
                if has_speech and volume > silence_threshold * 1.5:
                    silence_counter = max(0, silence_counter - frames // 2)  # Decay slowly

        with sd.InputStream(callback=callback, channels=1,
                           samplerate=self.sample_rate, dtype='float32'):
            # Record until duration or silence detected
            while len(recording) < duration * self.sample_rate / 1024:
                sd.sleep(100)
                # Only stop on silence if we've heard speech first
                if has_speech and silence_counter > silence_samples:
                    print("\n\n🔇 6 seconds of silence detected - stopping!")
                    break

        if not recording:
            return np.array([])

        audio = np.concatenate(recording, axis=0)
        print("✅ Recording complete")
        return audio

    def transcribe(self, audio):
        """
        Transcribe audio to text using Whisper

        Args:
            audio: numpy array with audio data

        Returns:
            Transcribed text
        """
        # Save temporary audio file
        temp_path = Path("temp_audio/temp.wav")
        temp_path.parent.mkdir(exist_ok=True)
        sf.write(temp_path, audio, self.sample_rate)

        # Transcribe
        print("🔄 Transcribing...")
        segments, info = self.model.transcribe(
            str(temp_path),
            language=self.language,
            vad_filter=True  # Voice Activity Detection
        )

        # Combine all segments
        text = " ".join([segment.text for segment in segments])

        # Cleanup
        temp_path.unlink()

        return text.strip()

    def record_audio_manual(self, max_duration=60):
        """
        Record audio with MANUAL control - press Enter to stop
        NO automatic silence detection!

        Args:
            max_duration: Maximum recording time in seconds

        Returns:
            numpy array with audio data
        """
        import threading

        print("🎤 Recording started!")
        print("🔴 Press ENTER when you finish speaking to stop recording")
        print()

        recording = []
        is_recording = True

        def callback(indata, frames, time, status):
            if is_recording:
                recording.append(indata.copy())
                # Visual feedback
                if len(recording) % (self.sample_rate // 2) == 0:
                    elapsed = len(recording) / self.sample_rate * 1024
                    print(f"🗣️  Recording... {elapsed:.0f}s", end="\r", flush=True)

        def wait_for_enter():
            nonlocal is_recording
            input()  # Wait for Enter key
            is_recording = False
            print("\n✋ Stopping recording...")

        # Start thread waiting for Enter key
        enter_thread = threading.Thread(target=wait_for_enter, daemon=True)
        enter_thread.start()

        with sd.InputStream(callback=callback, channels=1,
                           samplerate=self.sample_rate, dtype='float32'):
            # Record until Enter pressed or max duration
            start_time = 0
            while is_recording and start_time < max_duration:
                sd.sleep(100)
                start_time += 0.1

            if start_time >= max_duration:
                print(f"\n⏱️  Max duration ({max_duration}s) reached, stopping...")

        if not recording:
            return np.array([])

        audio = np.concatenate(recording, axis=0)
        duration = len(audio) / self.sample_rate
        print(f"✅ Recorded {duration:.1f} seconds\n")
        return audio

    def listen_and_transcribe(self, duration=10):
        """
        Record audio and transcribe in one step

        Returns:
            Transcribed text
        """
        audio = self.record_audio(duration=duration)
        text = self.transcribe(audio)
        return text

    def listen_and_transcribe_manual(self, max_duration=60):
        """
        Record audio with MANUAL control and transcribe

        Returns:
            Transcribed text
        """
        audio = self.record_audio_manual(max_duration=max_duration)
        if len(audio) == 0:
            return ""
        text = self.transcribe(audio)
        return text


if __name__ == "__main__":
    # Test the STT module
    stt = SpeechToText(model_size="base")

    print("\n" + "="*50)
    print("Testing Speech-to-Text")
    print("="*50 + "\n")

    text = stt.listen_and_transcribe(duration=5)
    print(f"\n📝 You said: {text}")

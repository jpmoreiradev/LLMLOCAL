#!/usr/bin/env python3
"""
Test script to verify all components are working
"""

import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def test_imports():
    """Test if all required packages can be imported"""
    console.print("\n[bold cyan]Testing Python imports...[/bold cyan]")

    tests = [
        ("yaml", "PyYAML"),
        ("sounddevice", "sounddevice"),
        ("soundfile", "soundfile"),
        ("numpy", "numpy"),
        ("rich", "rich"),
        ("ollama", "ollama"),
    ]

    passed = 0
    failed = 0

    for module, name in tests:
        try:
            __import__(module)
            console.print(f"  ✅ {name}")
            passed += 1
        except ImportError as e:
            console.print(f"  ❌ {name}: {e}")
            failed += 1

    # Optional imports
    try:
        import faster_whisper
        console.print("  ✅ faster-whisper")
        passed += 1
    except ImportError:
        console.print("  ⚠️  faster-whisper (optional, will use openai-whisper)")

    return passed, failed


def test_audio():
    """Test audio devices"""
    console.print("\n[bold cyan]Testing audio setup...[/bold cyan]")

    try:
        import sounddevice as sd
        devices = sd.query_devices()

        # Find default input device
        default_input = sd.default.device[0]
        input_device = devices[default_input]

        console.print(f"  ✅ Microphone found: {input_device['name']}")
        return True
    except Exception as e:
        console.print(f"  ❌ Audio error: {e}")
        return False


def test_ollama():
    """Test Ollama connection"""
    console.print("\n[bold cyan]Testing Ollama (LLM)...[/bold cyan]")

    try:
        import ollama

        # Check if llama3 is available
        try:
            models = ollama.list()
            # Handle both dict formats (with or without 'models' key)
            if isinstance(models, dict):
                model_list = models.get('models', [])
            else:
                model_list = models

            model_names = [m.get('name', '') if isinstance(m, dict) else str(m) for m in model_list]

            if any('llama3' in name for name in model_names):
                console.print("  ✅ LLaMA 3 model found")
                return True
            else:
                console.print("  ⚠️  LLaMA 3 not found. Run: ollama pull llama3")
                return False
        except Exception as inner_e:
            # Fallback: try to run a simple test
            try:
                ollama.show('llama3')
                console.print("  ✅ LLaMA 3 model found")
                return True
            except:
                console.print("  ⚠️  LLaMA 3 not found. Run: ollama pull llama3")
                return False
    except Exception as e:
        console.print(f"  ❌ Ollama error: {e}")
        console.print("  💡 Make sure Ollama is installed and running")
        return False


def test_tts():
    """Test TTS availability"""
    console.print("\n[bold cyan]Testing Text-to-Speech...[/bold cyan]")

    import os

    if os.system("which espeak > /dev/null 2>&1") == 0:
        console.print("  ✅ espeak found")
        return True
    elif os.system("which say > /dev/null 2>&1") == 0:
        console.print("  ✅ macOS say found")
        return True
    else:
        console.print("  ⚠️  No TTS found (voice output will be disabled)")
        return False


def test_config():
    """Test configuration file"""
    console.print("\n[bold cyan]Testing configuration...[/bold cyan]")

    from pathlib import Path
    import yaml

    config_path = Path("config/settings.yaml")

    if not config_path.exists():
        console.print("  ❌ config/settings.yaml not found")
        return False

    try:
        with open(config_path) as f:
            config = yaml.safe_load(f)
        console.print("  ✅ Configuration file valid")
        return True
    except Exception as e:
        console.print(f"  ❌ Config error: {e}")
        return False


def main():
    """Run all tests"""
    console.print(Panel.fit(
        "[bold]🧪 English Training Assistant - Setup Test[/bold]",
        border_style="cyan"
    ))

    results = {}

    # Run tests
    passed, failed = test_imports()
    results['imports'] = (failed == 0)

    results['audio'] = test_audio()
    results['ollama'] = test_ollama()
    results['tts'] = test_tts()
    results['config'] = test_config()

    # Summary
    console.print("\n" + "="*50)
    console.print("[bold]Summary:[/bold]")

    all_passed = all(results.values())

    if all_passed:
        console.print("\n[bold green]✅ All tests passed! You're ready to go![/bold green]")
        console.print("\nRun the assistant with: [cyan]python main.py[/cyan]")
    else:
        console.print("\n[bold yellow]⚠️  Some tests failed[/bold yellow]")

        if not results['imports']:
            console.print("\n[yellow]→ Install missing packages: pip install -r requirements.txt[/yellow]")

        if not results['ollama']:
            console.print("\n[yellow]→ Install Ollama: curl -fsSL https://ollama.com/install.sh | sh[/yellow]")
            console.print("[yellow]→ Download model: ollama pull llama3[/yellow]")

        if not results['audio']:
            console.print("\n[yellow]→ Check your microphone permissions[/yellow]")

        if not results['tts']:
            console.print("\n[yellow]→ Install espeak: sudo apt-get install espeak[/yellow]")
            console.print("[dim](TTS is optional, the assistant will work without it)[/dim]")

    console.print("\n")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
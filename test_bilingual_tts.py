#!/usr/bin/env python3
"""
Test bilingual TTS (Portuguese + English)
"""

from modules.tts import GoogleTTS

print("🎤 Testando TTS Bilíngue (PT + EN)\n")

tts = GoogleTTS()

# Test cases with mixed Portuguese and English
test_phrases = [
    "Ótimo! Agora tenta dizer em inglês: 'eu acordei cedo hoje'.",
    "Muito bem! Como se fala 'eu estou com fome' em inglês?",
    "Quase! A forma correta é 'I went'. Tenta de novo!",
    "Perfect! Now tell me about your family.",
    "Correto! What did you eat yesterday?",
]

for i, phrase in enumerate(test_phrases, 1):
    print(f"\n{i}. 🔊 Falando: {phrase}")
    print("-" * 60)
    tts.speak(phrase)
    print()

print("\n✅ Teste completo!")
print("\nO que deve acontecer:")
print("- Partes em português devem ser faladas em PT-BR")
print("- Partes entre aspas devem ser faladas em inglês")
print("- Deve soar natural em ambos os idiomas")
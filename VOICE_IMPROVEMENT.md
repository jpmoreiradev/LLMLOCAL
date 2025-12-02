## 🔊 Melhorando a Qualidade da Voz

Por padrão, o assistente usa **espeak** que tem voz robótica. Aqui estão as opções para melhorar:

## ✨ Opção 1: Google TTS (RECOMENDADO) - Voz Natural

### Instalação:

```bash
# 1. Instalar Google TTS
source venv/bin/activate
pip install gtts

# 2. Instalar player de áudio
sudo apt-get install mpg123 ffmpeg
```

### Como funciona:
- ✅ Voz **muito mais natural** (usa vozes reais do Google)
- ✅ Automático - o sistema detecta e usa se disponível
- ✅ Funciona offline depois de baixar
- ⚠️ Primeira vez baixa da internet (mas depois cacheia)

### Testar:
```bash
python test_tts.py
```

---

## 🎤 Opção 2: espeak-ng - Melhor que espeak padrão

```bash
sudo apt-get install espeak-ng
```

- Menos robótico que espeak normal
- Já está configurado no código
- Automático se espeak-ng estiver instalado

---

## 🚀 Instalação Rápida (Recomendado)

Execute os scripts prontos:

```bash
# Instalar tudo de uma vez
./install_ffmpeg.sh

# Depois instale o gTTS
source venv/bin/activate
pip install gtts
```

---

## 🧪 Testar a Qualidade

```bash
# Teste comparativo das vozes
source venv/bin/activate
python test_tts.py
```

Você ouvirá:
1. **Google TTS** - Voz natural
2. **espeak** - Voz robótica (fallback)

---

## 🔧 Prioridade Automática

O sistema tenta usar nesta ordem:

1. **GoogleTTS** (melhor qualidade) ⭐
2. **Piper TTS** (boa qualidade, mas precisa instalar)
3. **espeak-ng** (melhorado)
4. **espeak** (fallback básico)

Você não precisa configurar nada - o sistema escolhe automaticamente o melhor disponível!

---

## ⚡ Instalação Express (Copiar e Colar)

```bash
# Instalar tudo de uma vez
sudo apt-get update
sudo apt-get install -y ffmpeg mpg123
source venv/bin/activate
pip install gtts
```

Depois rode:
```bash
python main.py
```

Pronto! A voz já está natural! 🎉

---

## 📊 Comparação

| Engine | Qualidade | Velocidade | Instalação |
|--------|-----------|------------|------------|
| **Google TTS** | ⭐⭐⭐⭐⭐ | Média | `pip install gtts` + `apt install mpg123 ffmpeg` |
| **Piper** | ⭐⭐⭐⭐ | Rápida | Complicada (não recomendado) |
| **espeak-ng** | ⭐⭐⭐ | Rápida | `apt install espeak-ng` |
| **espeak** | ⭐⭐ | Rápida | Já instalado |

---

## 🆘 Problemas Comuns

### "No such file or directory: 'mpg123'"
```bash
sudo apt-get install mpg123
```

### "ffprobe not found"
```bash
sudo apt-get install ffmpeg
```

### Voz ainda robótica
```bash
# Confirme que Google TTS está ativo
python test_tts.py
```

Se ver "Google TTS: Working", está tudo certo!

---

## 💡 Dica Pro

Para voz ainda mais lenta/clara (para iniciantes):

Edite [config/settings.yaml](config/settings.yaml):
```yaml
tts:
  speed: 0.8  # Mais devagar
```

Ou no código Python ([main.py](main.py:55)):
```python
self.tts = GoogleTTS(lang='en', slow=True)  # Modo lento
```
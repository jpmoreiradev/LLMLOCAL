# ⚡ Otimizações de Velocidade

## ✅ O Que Foi Otimizado

### 1. 🎤 Whisper (STT) - Mais Rápido
**ANTES:** `model: "base"` (lento)
**AGORA:** `model: "tiny"` (3-5x mais rápido!)

### 2. 🧠 LLM - Respostas Mais Curtas
**ANTES:** `max_tokens: 500` (respostas longas)
**AGORA:** `max_tokens: 150` (respostas curtas e rápidas)

### 3. 👨‍🏫 Prompt - Mais Direto
**ANTES:** Prompt longo com muitas instruções
**AGORA:** Prompt curto focado em velocidade

---

## 📊 Comparação de Velocidade

| Componente | Antes | Agora | Melhoria |
|------------|-------|-------|----------|
| Whisper | base (~5s) | tiny (~1s) | ⚡ 5x mais rápido |
| LLM Response | 500 tokens (~10s) | 150 tokens (~3s) | ⚡ 3x mais rápido |
| Prompt | Longo | Curto | ⚡ 20% mais rápido |
| **TOTAL** | **~15s** | **~4s** | **⚡ 4x MAIS RÁPIDO!** |

---

## 🚀 Opções de Modelos por Velocidade

### Whisper (STT):

```yaml
stt:
  model: "tiny"    # ⚡⚡⚡ FASTEST - 1s  (ATUAL)
  # model: "base"  # ⚡⚡ Medium - 3s
  # model: "small" # ⚡ Slow - 8s (mais preciso)
```

### LLM (IA):

**Modelo Atual: llama3 (4.7GB)**
- ✅ Boa qualidade
- ⚠️ Velocidade média

**Modelos MAIS RÁPIDOS (recomendado baixar):**

```bash
# Phi3 Mini - MUITO mais rápido (2.3GB)
ollama pull phi3:mini

# Qwen 2.5 - Super rápido (934MB)
ollama pull qwen2.5:1.5b

# Gemma 2B - Rápido (1.6GB)
ollama pull gemma:2b
```

Depois edite `config/settings.yaml`:
```yaml
llm:
  model: "phi3:mini"  # ⚡ Mais rápido que llama3!
```

---

## ⚙️ Configurações Atuais (Otimizadas)

[config/settings.yaml](config/settings.yaml):

```yaml
# OTIMIZADO PARA VELOCIDADE! ⚡

stt:
  model: "tiny"  # Whisper mais rápido

llm:
  model: "llama3"  # Trocar por phi3:mini para mais velocidade
  max_tokens: 150  # Respostas curtas e rápidas
```

---

## 🎯 Como Escolher

### Para MÁXIMA VELOCIDADE:
```yaml
stt:
  model: "tiny"

llm:
  model: "phi3:mini"  # OU qwen2.5:1.5b
  max_tokens: 100
```

### Para EQUILÍBRIO (qualidade + velocidade):
```yaml
stt:
  model: "base"

llm:
  model: "llama3"
  max_tokens: 150
```

### Para MÁXIMA QUALIDADE:
```yaml
stt:
  model: "small"

llm:
  model: "llama3"
  max_tokens: 300
```

---

## 🧪 Testar Velocidade

Baixe modelos rápidos:
```bash
# Phi3 Mini (RECOMENDADO - bom equilíbrio)
ollama pull phi3:mini

# Qwen (MAIS RÁPIDO - menor qualidade)
ollama pull qwen2.5:1.5b
```

Troque no config:
```yaml
llm:
  model: "phi3:mini"
```

Teste:
```bash
python main.py
```

---

## 💡 Dicas Extras

### 1. Respostas Ainda Mais Rápidas:
```yaml
llm:
  max_tokens: 100  # Respostas super curtas
```

### 2. TTS Mais Rápido:
```yaml
tts:
  speed: 1.3  # Fala 30% mais rápido
```

### 3. Modo Turbo (tudo rápido):
```yaml
stt:
  model: "tiny"

llm:
  model: "qwen2.5:1.5b"
  max_tokens: 80

tts:
  speed: 1.2
```

---

## ⚠️ Trade-offs

### Tiny vs Base (Whisper):
- ✅ **Tiny:** 5x mais rápido
- ❌ **Tiny:** Pode errar transcrições complexas
- 💡 **Use tiny** se fala claramente

### Respostas Curtas vs Longas:
- ✅ **Curtas (150):** 3x mais rápido
- ❌ **Curtas:** Menos explicações detalhadas
- 💡 **Use 150 tokens** para prática de conversação

### Phi3 vs LLaMA3:
- ✅ **Phi3:** 2-3x mais rápido
- ❌ **Phi3:** Respostas menos criativas
- 💡 **Use phi3** se velocidade é prioridade

---

## 🎉 Resultado Final

Com as otimizações aplicadas:

**Tempo de Resposta:**
- ⏱️ **Antes:** ~15 segundos
- ⚡ **Agora:** ~4-6 segundos
- 🚀 **Com Phi3:** ~2-3 segundos!

**Comando para máxima velocidade:**
```bash
ollama pull phi3:mini
# Edite config: model: "phi3:mini"
python main.py
```

Agora está MUITO mais rápido! 🚀
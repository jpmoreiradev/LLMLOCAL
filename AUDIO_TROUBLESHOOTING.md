# 🎤 Problemas de Áudio - Soluções

## Problema: "Ele corta minha fala muito cedo"

### ✅ RESOLVIDO!

Acabamos de ajustar o sistema para:
- ✅ Esperar **3.5 segundos de silêncio** antes de parar (era 2s)
- ✅ Só parar depois de detectar que você falou algo
- ✅ Threshold de silêncio mais baixo (mais sensível)

### Como testar se funcionou:

```bash
source venv/bin/activate
python test_audio.py
```

Escolha opção **2** para testar gravação completa.

---

## 🔧 Ajustes Manuais (se ainda cortar)

### Opção 1: Aumentar tempo de silêncio

Edite [config/settings.yaml](config/settings.yaml):

```yaml
audio:
  max_silence_duration: 5.0  # Aumentar para 5 segundos
```

### Opção 2: Tornar menos sensível ao silêncio

Edite [config/settings.yaml](config/settings.yaml):

```yaml
audio:
  silence_threshold: 0.003  # Menor = mais sensível
```

### Opção 3: Aumentar tempo máximo de gravação

Edite [config/settings.yaml](config/settings.yaml):

```yaml
audio:
  max_recording_time: 60  # Aumentar para 60 segundos
```

---

## 🧪 Ferramentas de Diagnóstico

### 1. Teste de Volume do Microfone

```bash
python test_audio.py
# Escolha opção 1
```

Isso mostra em tempo real o volume do seu microfone.

**O que você deve ver:**
- 🟢 LOUD/GOOD quando falando
- 🔴 SILENT quando em silêncio

**Se sempre aparecer SILENT:**
- Aumente volume do microfone no sistema
- Fale mais perto do microfone
- Verifique se o microfone certo está selecionado

### 2. Teste Completo de Gravação

```bash
python test_audio.py
# Escolha opção 2
```

Simula exatamente como o assistente grava.

**Resultados esperados:**
- Deve gravar até você parar de falar
- Deve transcrever o que você disse
- Se cortar rápido demais → ajuste `max_silence_duration`

---

## 📊 Valores Recomendados

### Para fala rápida/fluente:
```yaml
audio:
  silence_threshold: 0.005
  max_silence_duration: 2.5
  max_recording_time: 30
```

### Para pausas longas (pensando):
```yaml
audio:
  silence_threshold: 0.005
  max_silence_duration: 5.0  # ⭐
  max_recording_time: 45
```

### Para ambiente barulhento:
```yaml
audio:
  silence_threshold: 0.01  # Menos sensível
  max_silence_duration: 3.0
  max_recording_time: 30
```

### Para ambiente silencioso:
```yaml
audio:
  silence_threshold: 0.003  # Mais sensível
  max_silence_duration: 3.5
  max_recording_time: 30
```

---

## 🔍 Outros Problemas Comuns

### "Não detecta nada que eu falo"

**Solução:**
1. Verifique se microfone está funcionando no sistema
2. Liste dispositivos de áudio:
```bash
python -c "import sounddevice; print(sounddevice.query_devices())"
```
3. Teste volume em tempo real:
```bash
python test_audio.py
```

### "Detecta barulho de fundo como fala"

**Solução:**
Aumente o threshold de silêncio em [config/settings.yaml](config/settings.yaml):
```yaml
audio:
  silence_threshold: 0.015  # Mais alto = menos sensível
```

### "Grava muito além do que eu falo"

**Solução:**
Diminua o tempo de silêncio:
```yaml
audio:
  max_silence_duration: 2.0  # Para mais rápido
```

---

## 💡 Dicas para Melhor Gravação

1. **Fale naturalmente** - não precisa gritar
2. **Ambiente silencioso** - menos barulho de fundo
3. **Boa distância** - 20-30cm do microfone
4. **Pause claramente** - ao terminar, fique 3-4 segundos em silêncio
5. **Fale devagar** - especialmente se iniciante

---

## 🆘 Ajuda Personalizada

Se ainda tiver problemas:

1. Rode o teste de diagnóstico:
```bash
python test_audio.py
```

2. Veja os valores que apareceram

3. Ajuste baseado nisso:
   - Volume muito baixo (<0.005)? → Aumente volume do mic
   - Para muito rápido? → Aumente `max_silence_duration`
   - Não para nunca? → Diminua `max_silence_duration`

---

## ✨ Melhorias Aplicadas

**O que mudamos para você:**

| Antes | Agora | Efeito |
|-------|-------|--------|
| 2.0s de silêncio | 3.5s de silêncio | ⏱️ Mais tempo para pensar |
| Parava mesmo sem fala | Só para depois de ouvir você | 🎤 Não corta no início |
| Threshold fixo | Threshold configurável | ⚙️ Personalizável |
| Sem feedback | Mensagens claras | 📢 Você sabe o que está acontecendo |

Agora teste rodando:
```bash
python main.py
```

Deve funcionar muito melhor! 🚀
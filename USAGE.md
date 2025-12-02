# 🎯 Usage Guide

How to use your English Training Voice Assistant effectively.

## Starting the Assistant

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Run the assistant
python main.py
```

## Basic Conversation Flow

1. **Press Enter** when ready to speak
2. **Speak in English** (you have 30 seconds max)
3. **Listen** to the AI's response
4. **Repeat!**

## Example Conversation

```
🤖 Teacher: Hello! I'm your English teacher. Let's have a conversation!
            What would you like to talk about today?

[Press Enter]

👤 You: Hi! I want to talk about my weekend.

🤖 Teacher: Great! I'd love to hear about it. What did you do this weekend?

[Press Enter]

👤 You: Yesterday I go to the park with my friends.

🤖 Teacher: That sounds fun! Just a small correction: "Yesterday I *went*
            to the park" (past tense of 'go' is 'went').
            What did you do at the park?
```

## Commands

During conversation, you can say:

- **"exit"** / **"quit"** / **"goodbye"** - End the session
- **"summary"** - Get feedback on your conversation

## Configuration

Edit [config/settings.yaml](config/settings.yaml) to customize:

### Student Level

```yaml
student:
  level: "beginner"  # beginner, intermediate, advanced
```

- **Beginner:** Simple vocabulary, slower pace, more corrections
- **Intermediate:** Normal conversation, moderate corrections
- **Advanced:** Complex topics, minimal corrections

### Correction Style

```yaml
corrections:
  style: "friendly"  # strict, friendly, minimal
```

- **strict:** Corrects every mistake immediately
- **friendly:** Balances correction with encouragement (recommended)
- **minimal:** Only corrects major mistakes

### Topics

```yaml
student:
  topics:
    - daily_life
    - work
    - travel
    - technology
    - sports
    - movies
    # Add your own!
```

The AI will naturally steer conversations toward these topics.

### Voice Settings

```yaml
tts:
  enabled: true    # Set to false to disable voice
  speed: 1.0       # 0.5 = slower, 1.5 = faster
```

### Recording Time

```yaml
audio:
  max_recording_time: 30  # Maximum seconds per turn
  silence_threshold: 500  # ms of silence before stopping
```

## Tips for Better Practice

### 🎯 Set Clear Goals

Before starting, decide what you want to practice:
- Pronunciation of specific sounds
- Using past tense correctly
- Talking about work/travel
- Building vocabulary on a topic

### 🗣️ Speak Naturally

- Don't overthink - just speak!
- Make mistakes - that's how you learn
- Use gestures even though it's voice-only (helps fluency)

### 🎧 Listen Carefully

- Pay attention to how the AI pronounces words
- Notice the grammar structures used
- Try to repeat phrases you hear

### 📝 Review Your Sessions

```bash
# Your conversations are saved in history/
ls history/

# View a session
cat history/session_20250101_120000.json
```

Each session includes:
- Full conversation transcript
- Corrections made
- Summary and feedback

### 🔁 Practice Regularly

- **Daily:** 10-15 minutes (best for retention)
- **3x/week:** 20-30 minutes
- **Weekly:** 45-60 minutes

Consistency beats intensity!

## Advanced Usage

### Using Different LLM Models

```bash
# List available models
ollama list

# Pull a new model
ollama pull mistral

# Update config
# Edit config/settings.yaml: model: "mistral"
```

**Model recommendations:**
- **llama3** - Best overall (default)
- **mistral** - Fast and good quality
- **phi3:mini** - Fastest for low-end systems
- **gemma2** - Google's model, good for conversations

### Multiple Conversation Modes

Create different config files for different practice modes:

```bash
# Copy default config
cp config/settings.yaml config/business.yaml

# Edit for business English
# Change topics to: work, meetings, presentations, networking

# Run with specific config
python main.py --config config/business.yaml
```

### Batch Practice Sessions

```bash
# Run 3 sessions in a row with breaks
for i in {1..3}; do
  echo "Session $i/3"
  python main.py
  echo "Take a 5-minute break..."
  sleep 300
done
```

## Troubleshooting

### AI doesn't hear me

- Check microphone permissions
- Speak louder or closer to mic
- Reduce `silence_threshold` in config

### AI talks too fast

```yaml
tts:
  speed: 0.8  # Slower speech
```

### Conversations are too easy/hard

```yaml
student:
  level: "advanced"  # Or "beginner"
```

### Want more/fewer corrections

```yaml
corrections:
  style: "strict"   # More corrections
  # or
  style: "minimal"  # Fewer corrections
```

## Example Practice Routines

### Morning Routine (10 min)

1. Talk about your plans for the day
2. Practice using future tense
3. Review yesterday's mistakes

### Vocabulary Building (15 min)

1. Choose a topic (e.g., "cooking")
2. Try to use 10 new words
3. Ask the AI to explain words you don't know

### Pronunciation Focus (20 min)

1. Practice difficult sounds (th, r, v, etc.)
2. Ask AI: "How do you pronounce 'schedule'?"
3. Repeat after the AI

### Free Conversation (30 min)

1. No specific goal
2. Talk about anything
3. Let the conversation flow naturally

## Getting the Most Value

✅ **Do:**
- Practice consistently
- Make mistakes freely
- Ask for clarification
- Review your progress

❌ **Don't:**
- Get frustrated with corrections
- Speak in Portuguese
- Give up after one session
- Skip reviewing past conversations

## What's Next?

After you're comfortable:

1. Increase difficulty level
2. Try more complex topics
3. Practice specific scenarios (job interview, travel, etc.)
4. Set pronunciation challenges

Happy learning! 🎓

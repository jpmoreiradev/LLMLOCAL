"""
LLM module using Ollama
Handles conversation and provides corrections
"""

import ollama
from pathlib import Path


class EnglishTeacher:
    def __init__(self, model="llama3", temperature=0.7):
        """
        Initialize the English teacher LLM

        Args:
            model: Ollama model name (llama3, mistral, phi3, etc.)
            temperature: Creativity level (0.0-1.0)
        """
        self.model = model
        self.temperature = temperature
        self.conversation_history = []

        # Load system prompt
        prompt_path = Path("prompts/teacher.txt")
        if prompt_path.exists():
            self.system_prompt = prompt_path.read_text()
        else:
            self.system_prompt = "You are a friendly English teacher helping students practice conversation."

        print(f"✅ English teacher ready (model: {model})")

    def chat(self, user_message):
        """
        Send message to the teacher and get response

        Args:
            user_message: What the student said

        Returns:
            Teacher's response with corrections
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        # Prepare messages for API
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history

        # Get response from Ollama
        print("🤔 Teacher is thinking...")
        response = ollama.chat(
            model=self.model,
            messages=messages,
            options={
                "temperature": self.temperature,
                "num_predict": 500
            }
        )

        teacher_response = response['message']['content']

        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": teacher_response
        })

        return teacher_response

    def reset_conversation(self):
        """Start a new conversation"""
        self.conversation_history = []
        print("🔄 Conversation reset")

    def get_conversation_summary(self):
        """
        Get a summary of the conversation for review

        Returns:
            Summary of what was practiced
        """
        if not self.conversation_history:
            return "No conversation yet."

        summary_prompt = """
        Based on this conversation, provide a brief summary:
        1. Main topics discussed
        2. Common mistakes made
        3. Areas for improvement
        4. Positive points

        Keep it concise and encouraging.
        """

        messages = [
            {"role": "system", "content": "You are an English teacher providing conversation feedback."}
        ] + self.conversation_history + [
            {"role": "user", "content": summary_prompt}
        ]

        response = ollama.chat(
            model=self.model,
            messages=messages
        )

        return response['message']['content']


if __name__ == "__main__":
    # Test the LLM module
    teacher = EnglishTeacher()

    print("\n" + "="*50)
    print("Testing English Teacher LLM")
    print("="*50 + "\n")

    # Simulate conversation
    test_messages = [
        "Hello! I want practice my English",
        "Yesterday I go to the beach with my friends",
        "We play volleyball and swim in the ocean"
    ]

    for msg in test_messages:
        print(f"\n👤 Student: {msg}")
        response = teacher.chat(msg)
        print(f"👨‍🏫 Teacher: {response}")

    print("\n" + "="*50)
    print("Conversation Summary")
    print("="*50 + "\n")
    summary = teacher.get_conversation_summary()
    print(summary)

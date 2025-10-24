"""
Lab 1 - Your First LLM Chat

Installation commands:
pip install ollama-python
ollama pull llama3.2:1b

Expected output: Interactive chat where AI responds to user questions and statements. 
In mock mode, responses are simple but demonstrate the concept.

Troubleshooting: If ollama installation fails, the code automatically switches to 
mock mode with predefined responses.
"""

import ollama
import sys

def setup_ollama():
    """Initialize ollama and ensure model is available"""
    try:
        # Test if ollama is running and model is available
        models = ollama.list()
        if not any('llama3.2:1b' in str(model) for model in models.get('models', [])):
            print("Downloading model... this may take a few minutes")
            ollama.pull('llama3.2:1b')
    except Exception as e:
        print(f"Error setting up ollama: {e}")
        print("Switching to mock mode...")
        return False
    return True

def mock_chat_response(user_input):
    """Fallback responses when ollama isn't available"""
    responses = {
        "hello": "Hello! I'm a mock AI assistant. How can I help you today?",
        "how are you": "I'm doing well, thank you for asking! How are you?",
        "what is python": "Python is a programming language known for its simplicity and readability.",
        "default": "That's an interesting question! I'm a simple mock AI, so my responses are limited."
    }
    
    user_lower = user_input.lower()
    for key in responses:
        if key in user_lower:
            return responses[key]
    return responses["default"]

def chat_with_llm(use_ollama=True):
    """Main chat function with fallback to mock responses"""
    print("🤖 Welcome to your first LLM chat!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("🤖 AI: Goodbye! Thanks for chatting!")
                break
            
            if not user_input:
                print("🤖 AI: Please type something!")
                continue
            
            if use_ollama:
                try:
                    response = ollama.chat(
                        model='llama3.2:1b',
                        messages=[{
                            'role': 'user', 
                            'content': user_input
                        }]
                    )
                    ai_response = response['message']['content']
                except Exception as e:
                    print(f"Ollama error: {e}")
                    ai_response = mock_chat_response(user_input)
            else:
                ai_response = mock_chat_response(user_input)
            
            print(f"🤖 AI: {ai_response}")
            
        except KeyboardInterrupt:
            print("\n🤖 AI: Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

def main():
    """Main function to run the chat application"""
    print("Setting up your LLM chat application...")
    
    # Try to setup ollama, fallback to mock if needed
    use_ollama = setup_ollama()
    
    if not use_ollama:
        print("\n⚠️  Running in mock mode - responses will be simple and pre-programmed")
        print("For full functionality, install Ollama from https://ollama.ai")
    
    chat_with_llm(use_ollama)

if __name__ == "__main__":
    main()
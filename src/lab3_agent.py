"""
Lab 3 - Simple AI Agent

A simplified AI agent that can use basic tools to help users.
Uses simple keyword detection to avoid LLM hallucinations.

Expected output: AI agent that analyzes user requests and chooses appropriate tools 
(calculator, search, time, random number) to accomplish tasks.
"""

import ollama
import random
import re
from datetime import datetime

def setup_ollama():
    """Initialize ollama - same as previous labs"""
    try:
        models = ollama.list()
        if not any('llama3.2:1b' in str(model) for model in models.get('models', [])):
            print("Downloading model... this may take a few minutes")
            ollama.pull('llama3.2:1b')
        return True
    except Exception as e:
        print(f"Error setting up ollama: {e}")
        return False

class SimpleAgent:
    """A simple AI agent with basic tools"""
    
    def __init__(self, use_ollama=True):
        self.use_ollama = use_ollama
    
    def calculator(self, expression):
        """Simple calculator tool - handles basic math"""
        try:
            # Clean the expression and allow basic math characters
            clean_expr = re.sub(r'[^0-9+\-*/().\s]', '', expression)
            if clean_expr.strip():
                result = eval(clean_expr)
                return f"📊 {clean_expr} = {result}"
            else:
                return "❌ Invalid mathematical expression"
        except Exception as e:
            return f"❌ Calculation error: {e}"
    
    def web_search(self, query):
        """Simulated web search - returns mock results"""
        mock_results = {
            "weather": "🌤️ Current weather: 72°F, sunny with light clouds",
            "news": "📰 Top news: Technology sector shows growth, new AI developments announced", 
            "python": "🐍 Python is a programming language known for simplicity and versatility",
            "ai": "🤖 Artificial Intelligence refers to computer systems that perform human-like tasks"
        }
        
        query_lower = query.lower()
        for key in mock_results:
            if key in query_lower:
                return mock_results[key]
        
        return f"🔍 Search results for '{query}': Found general information about this topic"
    
    def current_time(self):
        """Get current time"""
        now = datetime.now()
        return f"🕒 Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def random_number(self, range_str="1-100"):
        """Generate random number in specified range"""
        try:
            if "-" in range_str:
                start, end = map(int, range_str.split("-"))
            else:
                start, end = 1, 100
            
            result = random.randint(start, end)
            return f"🎲 Random number ({start}-{end}): {result}"
        except:
            result = random.randint(1, 100)
            return f"🎲 Random number (1-100): {result}"

    def detect_intent(self, user_request):
        """Simple keyword-based intent detection"""
        request_lower = user_request.lower()
        
        # Math calculation keywords
        if any(word in request_lower for word in ['calculate', 'math', 'compute', '+', '-', '*', '/', 'multiply', 'divide', 'add', 'subtract']):
            # Extract mathematical expression
            math_match = re.search(r'[\d\s+\-*/().]+', user_request)
            if math_match:
                return 'calculator', math_match.group().strip()
            else:
                return 'calculator', user_request
        
        # Search keywords  
        elif any(word in request_lower for word in ['search', 'find', 'look up', 'weather', 'news', 'python', 'ai']):
            return 'web_search', user_request
            
        # Time keywords
        elif any(word in request_lower for word in ['time', 'date', 'clock', 'now']):
            return 'current_time', ''
            
        # Random number keywords
        elif any(word in request_lower for word in ['random', 'number', 'dice', 'roll']):
            # Extract range if specified
            range_match = re.search(r'(\d+)[-\s]?(?:to|and)?[-\s]?(\d+)', user_request)
            if range_match:
                return 'random_number', f"{range_match.group(1)}-{range_match.group(2)}"
            else:
                return 'random_number', '1-100'
        
        else:
            return 'chat', user_request

    def execute_tool(self, tool_name, params):
        """Execute the specified tool with parameters"""
        if tool_name == 'calculator':
            return self.calculator(params)
        elif tool_name == 'web_search':
            return self.web_search(params)
        elif tool_name == 'current_time':
            return self.current_time()
        elif tool_name == 'random_number':
            return self.random_number(params)
        elif tool_name == 'chat':
            return self.chat_response(params)
        else:
            return "❌ Unknown tool requested"

    def chat_response(self, user_request):
        """Generate a chat response using LLM or fallback"""
        if not self.use_ollama:
            return "💬 Hello! I can help you with calculations, searches, time, and random numbers. What would you like to do?"
        
        try:
            response = ollama.chat(
                model='llama3.2:1b',
                messages=[{
                    'role': 'user', 
                    'content': f"You are a helpful assistant. Respond briefly to: {user_request}"
                }]
            )
            return f"💬 {response['message']['content'].strip()}"
        except Exception as e:
            return "💬 I'm here to help! I can calculate math, search for info, tell time, or generate random numbers."

    def process_request(self, user_request):
        """Main method to process user requests"""
        # Detect what the user wants to do
        intent, params = self.detect_intent(user_request)
        
        # Execute the appropriate tool
        return self.execute_tool(intent, params)

def interactive_agent_demo(use_ollama=True):
    """Interactive demo of the AI agent"""
    
    agent = SimpleAgent(use_ollama)
    
    print("🤖 Simple AI Agent")
    print("=" * 40)
    print("I can help you with:")
    print("• 📊 Math calculations (calculate 25 * 17)")
    print("• 🔍 Information searches (search for Python)")
    print("• 🕒 Current time (what time is it?)")
    print("• 🎲 Random numbers (give me a random number)")
    print("• 💬 General chat")
    print()
    print("Type 'quit' to exit")
    print("-" * 40)
    
    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Agent: Goodbye! Thanks for using the AI agent!")
                break
            
            if not user_input:
                print("🤖 Agent: Please type something!")
                continue
            
            # Process the request
            response = agent.process_request(user_input)
            print(f"🤖 Agent: {response}")
            
        except KeyboardInterrupt:
            print("\n🤖 Agent: Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            continue

def main():
    """Main function"""
    print("Setting up Simple AI Agent...")
    
    use_ollama = setup_ollama()
    
    if not use_ollama:
        print("⚠️  Running in basic mode (no LLM for chat)")
    
    interactive_agent_demo(use_ollama)

if __name__ == "__main__":
    main()
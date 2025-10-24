"""
Lab 2 - Smart Question Answerer

Uses same ollama setup as Lab 1
No additional installations needed

Expected output: System that accurately answers questions based on provided context. 
Will say "cannot answer" for questions not covered in the context.

Troubleshooting: Mock mode provides simple keyword-based matching when ollama is 
unavailable, demonstrating the concept with limited functionality.
"""

import ollama
import json

def setup_ollama():
    """Initialize ollama - same as Lab 1"""
    try:
        models = ollama.list()
        if not any('llama3.2:1b' in str(model) for model in models.get('models', [])):
            print("Downloading model... this may take a few minutes")
            ollama.pull('llama3.2:1b')
        return True
    except Exception as e:
        print(f"Error setting up ollama: {e}")
        return False

def mock_answer_question(context, question):
    """Mock Q&A for when ollama isn't available"""
    context_lower = context.lower()
    question_lower = question.lower()
    
    # Simple keyword matching for demo
    if "python" in question_lower and "python" in context_lower:
        if "created" in question_lower or "made" in question_lower:
            return "According to the context, Python was created by Guido van Rossum."
        elif "when" in question_lower or "year" in question_lower:
            return "Based on the context, Python was created in 1991."
    
    if "capital" in question_lower:
        words = context_lower.split()
        try:
            capital_idx = words.index("capital")
            if capital_idx + 3 < len(words):
                return f"The capital appears to be {words[capital_idx + 3].title()}."
        except ValueError:
            pass
    
    return "I can see your question, but I need the full LLM to provide accurate answers from the context."

def answer_question_with_context(context, question, use_ollama=True):
    """Answer questions based on provided context"""
    
    if not use_ollama:
        return mock_answer_question(context, question)
    
    prompt = f"""Context: {context}

Question: {question}

Instructions: Answer the question based ONLY on the information provided in the context above. If the answer is not in the context, say "I cannot answer this question based on the provided context."

Answer:"""

    try:
        response = ollama.chat(
            model='llama3.2:1b',
            messages=[{
                'role': 'user', 
                'content': prompt
            }]
        )
        return response['message']['content'].strip()
    except Exception as e:
        print(f"Error with ollama: {e}")
        return mock_answer_question(context, question)

def interactive_qa_system(use_ollama=True):
    """Interactive question-answering system"""
    
    # Sample contexts for demonstration
    sample_contexts = {
        "Python Programming": """
        Python is a high-level programming language created by Guido van Rossum 
        and first released in 1991. It emphasizes code readability and simplicity. 
        Python supports multiple programming paradigms including procedural, 
        object-oriented, and functional programming. It has a large standard library 
        and is widely used for web development, data science, artificial intelligence, 
        and automation.
        """,
        
        "World Capitals": """
        France's capital is Paris, which is located in the north-central part of the country.
        Germany's capital is Berlin, which became the capital after reunification in 1990.
        Japan's capital is Tokyo, one of the world's most populous metropolitan areas.
        Australia's capital is Canberra, though Sydney and Melbourne are larger cities.
        """,
        
        "Climate Change": """
        Climate change refers to long-term shifts in global temperatures and weather patterns.
        The primary cause is human activities, particularly burning fossil fuels like coal and oil.
        This releases greenhouse gases such as carbon dioxide into the atmosphere.
        Effects include rising sea levels, more frequent extreme weather events, and ecosystem disruption.
        """
    }
    
    print("🔍 Smart Question Answering System")
    print("=" * 50)
    
    while True:
        print("\nAvailable contexts:")
        for i, topic in enumerate(sample_contexts.keys(), 1):
            print(f"{i}. {topic}")
        print("4. Use custom context")
        print("5. Quit")
        
        try:
            choice = input("\nSelect a context (1-5): ").strip()
            
            if choice == "5":
                print("Goodbye!")
                break
            elif choice == "4":
                context = input("\nEnter your custom context: ").strip()
                if not context:
                    print("Empty context provided!")
                    continue
            elif choice in ["1", "2", "3"]:
                topics = list(sample_contexts.keys())
                context = sample_contexts[topics[int(choice) - 1]]
                print(f"\nSelected context: {topics[int(choice) - 1]}")
                print(f"Context: {context[:100]}...")
            else:
                print("Invalid choice!")
                continue
            
            # Question-answering loop for selected context
            print(f"\n📝 Ask questions about this context (type 'back' to change context):")
            
            while True:
                question = input("\n❓ Your question: ").strip()
                
                if question.lower() == 'back':
                    break
                elif question.lower() in ['quit', 'exit']:
                    return
                elif not question:
                    print("Please enter a question!")
                    continue
                
                print("🤔 Thinking...")
                answer = answer_question_with_context(context, question, use_ollama)
                print(f"💡 Answer: {answer}")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

def main():
    """Main function"""
    print("Setting up Smart Question Answerer...")
    
    use_ollama = setup_ollama()
    
    if not use_ollama:
        print("\n⚠️  Running in mock mode")
        print("Answers will be basic keyword matching")
    
    interactive_qa_system(use_ollama)

if __name__ == "__main__":
    main()
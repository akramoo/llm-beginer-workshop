# Intro to LLMs & Agentic AI — Hands-on for Absolute Beginners

## Slide: Welcome to LLMs & Agentic AI

**Duration:** 3 minutes

**Speaker notes:** Welcome everyone! Today we'll explore Large Language Models and AI agents through hands-on coding. No prior AI experience needed. We'll build three simple projects together. Think of LLMs as very smart autocomplete that can have conversations and solve problems. By the end, you'll understand how AI assistants work and build your own mini-agent.

**In-class prompt:** Turn to someone near you and share: what's one AI tool you've used recently?

## Slide: Learning Objectives

**Duration:** 2 minutes

**Speaker notes:** By the end of this workshop, you'll be able to explain what LLMs are in simple terms, understand how AI agents work, write basic code to interact with language models, and identify real-world applications. These are foundational concepts for anyone interested in modern AI development.

**In-class prompt:** Which objective interests you most and why?

- Understand what Large Language Models (LLMs) are and how they work
- Grasp the concept of "agentic AI" and autonomous systems
- Write Python code to interact with language models
- Build a simple AI agent that can perform tasks
- Recognize ethical considerations and limitations

## Slide: Workshop Agenda & Timing

**Duration:** 2 minutes

**Speaker notes:** We'll balance theory with practice today. Notice we have three hands-on coding labs where you'll build progressively more complex AI systems. Each lab builds on the previous one. Don't worry if you fall behind - all code will be provided. The goal is understanding, not perfect execution.

**In-class prompt:** Any questions about the schedule before we dive in?

**9:00-9:15** — Introduction & Concepts (15 min)  
**9:15-9:35** — Lab 1: Your First LLM Chat (20 min)  
**9:35-9:55** — How LLMs Learn & Agent Basics (20 min)  
**9:55-10:15** — Lab 2: Smart Question Answerer (20 min)  
**10:15-10:25** — Break (10 min)  
**10:25-10:40** — Safety, Ethics & Real Examples (15 min)  
**10:40-11:05** — Lab 3: Simple AI Agent (25 min)  
**11:05-11:15** — Interactive Activities & Quiz (10 min)  
**11:15-11:20** — Recap & Next Steps (5 min)

## Slide: What is a Large Language Model?

**Duration:** 8 minutes

**Speaker notes:** Think of an LLM like a very smart autocomplete that read millions of books, websites, and documents. When you type something, it predicts what should come next based on patterns it learned. Unlike simple autocomplete, it understands context and can have conversations. It's not actually "thinking" like humans do - it's doing very sophisticated pattern matching.

**In-class prompt:** What's the difference between your phone's autocomplete and ChatGPT?

```python
# Simple analogy: autocomplete vs LLM
phone_autocomplete = "I am going to the..."  # suggests: store, park, movies
llm_response = "I am going to the..."  # can generate: "library to research medieval history for my thesis"

# LLMs understand context and generate coherent, relevant text
```

## Slide: How LLMs Learn (Training Overview)

**Duration:** 10 minutes

**Speaker notes:** LLMs learn in two main phases. First, they read massive amounts of text and learn to predict the next word - imagine reading every book ever written and becoming really good at finishing sentences. Then, humans give feedback on good vs bad responses to make them more helpful and safe. This is like having millions of teachers correct your homework.

**In-class prompt:** Why might an LLM sometimes give wrong answers if it learned from so much text?

```python
# Simplified training concept
training_data = [
    "The capital of France is Paris",
    "The capital of Spain is Madrid", 
    "The capital of Italy is Rome"
]

# Model learns patterns:
# "The capital of [COUNTRY] is [CITY]"

# Then it can answer: "The capital of Germany is ___"
```

## Slide: What is Agentic AI?

**Duration:** 8 minutes

**Speaker notes:** An AI agent is like giving an LLM hands and feet. Regular LLMs just chat. Agents can take actions - search the web, send emails, control other software. Think of it as the difference between a smart advisor who only talks versus a smart assistant who can actually do things for you. They can break down complex tasks into steps and execute them.

**In-class prompt:** Name one task you'd want an AI agent to handle for you automatically.

```python
# Regular LLM: just responds
user_input = "What's the weather like?"
llm_response = "I can't check current weather, but you could try a weather app"

# AI Agent: can take action
user_input = "What's the weather like?"
agent_actions = [
    "search_web('current weather')",
    "format_response(weather_data)"
]
agent_response = "It's 72°F and sunny in your location"
```

## Slide: Lab 1 - Your First LLM Chat

**Duration:** 20 minutes

**Goal:** Create a simple chatbot that responds to user input

**Speaker notes:** We'll use a local language model that runs on your laptop - no internet required. Walk through installing the library, loading a small model, and creating a basic chat loop. Emphasize that this is the foundation for all AI applications. Troubleshoot common installation issues as they arise.

**In-class prompt:** Try asking your chatbot about its favorite color or hobby - what happens?

```python
import ollama

# Simple chat with local LLM
def chat_with_llm():
    print("Chat with your LLM! Type 'quit' to exit")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
            
        response = ollama.chat(model='llama3.2:1b', messages=[
            {'role': 'user', 'content': user_input}
        ])
        
        print(f"AI: {response['message']['content']}")

chat_with_llm()
```

**Setup:** Install ollama, pull small model, run script  
**Expected output:** Interactive chat responses  
**Troubleshooting:** If model download fails, use mock responses

## Slide: Real-World LLM Applications

**Duration:** 5 minutes

**Speaker notes:** LLMs are everywhere now. Point out that each example represents billions of dollars in business value. These aren't just demos - they're transforming entire industries. The key insight is that text generation can solve many more problems than we initially realized, since so much work involves processing and creating text.

**In-class prompt:** Which application would be most useful in your daily life?

- Writing assistance (emails, documents, code)
- Customer service chatbots  
- Language translation
- Content summarization
- Code generation and debugging
- Creative writing and brainstorming
- Educational tutoring
- Medical documentation assistance
- Legal document analysis
- Research and fact-checking

## Slide: Lab 2 - Smart Question Answerer

**Duration:** 20 minutes

**Goal:** Build a system that answers questions about provided text

**Speaker notes:** This introduces the concept of context and retrieval. We're giving the LLM specific information to work with, rather than relying on its training data. This is how many real AI systems work - they combine retrieval with generation. Show how the same model becomes much more accurate when given relevant context.

**In-class prompt:** Try asking about something not in the provided text - what does the system do?

```python
# Question answering with context
def answer_questions(context, question):
    prompt = f"""
    Context: {context}
    
    Question: {question}
    
    Answer based only on the context provided:
    """
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']

# Example usage
context = "Python is a programming language created by Guido van Rossum in 1991."
question = "Who created Python?"
answer = answer_questions(context, question)
print(answer)
```

**Setup:** Extend previous ollama setup  
**Expected output:** Accurate answers from provided context  
**Troubleshooting:** Model may hallucinate - emphasize context constraints

## Slide: Safety, Ethics & Limitations

**Duration:** 10 minutes

**Speaker notes:** LLMs can be wrong, biased, or misused. They don't actually understand - they're very sophisticated pattern matchers. Always verify important information. Be aware of bias in training data. Consider privacy when sharing sensitive data with AI systems. The goal isn't to avoid AI, but to use it responsibly and understand its limitations.

**In-class prompt:** What's one risk of relying too heavily on AI-generated content?

- **Hallucination:** LLMs can confidently state false information
- **Bias:** Training data reflects societal biases
- **Privacy:** Sensitive data might be stored or misused
- **Over-reliance:** Critical thinking skills may atrophy
- **Job displacement:** Economic and social impacts
- **Misinformation:** Bad actors can generate fake content at scale

## Slide: Lab 3 - Simple AI Agent

**Duration:** 25 minutes

**Goal:** Create an agent that can use tools to accomplish tasks

**Speaker notes:** This is where it gets exciting - we're giving our LLM the ability to take actions. Start with simple tools like a calculator or web search simulator. Show how the agent can reason about which tool to use. This is the foundation of systems like ChatGPT plugins or autonomous AI assistants.

**In-class prompt:** What other tools would make this agent more useful?

```python
# Simple agent with tools
tools = {
    "calculator": lambda x: eval(x),  # Simplified - use safely in practice
    "web_search": lambda x: f"Search results for: {x}"
}

def agent_with_tools(user_request):
    # Agent decides which tool to use
    prompt = f"""
    User request: {user_request}
    Available tools: calculator, web_search
    
    Decide which tool to use and how, then provide the answer.
    """
    
    response = ollama.chat(model='llama3.2:1b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    
    return response['message']['content']

# Example usage
result = agent_with_tools("What is 25 * 17?")
print(result)
```

**Setup:** Build on previous labs  
**Expected output:** Agent chooses appropriate tools  
**Troubleshooting:** May need to guide tool selection manually

## Slide: Interactive Activities

**Duration:** 5 minutes

**Speaker notes:** These activities help cement understanding through peer discussion and hands-on exploration. Encourage students to share findings and ask questions. The goal is to connect technical concepts with practical applications and get everyone thinking creatively about AI possibilities.

**In-class prompt:** Pick one activity and spend 2 minutes exploring with a partner.

- **Pair up:** Explain LLMs to someone who's never heard of them (use analogies)
- **Group brainstorm:** List 5 problems an AI agent could solve in your daily life
- **Experiment:** Try to "break" your chatbot - what makes it confused?
- **Design challenge:** Sketch a workflow for an AI agent that helps with homework
- **Ethics discussion:** When should humans make decisions vs. AI systems?

## Slide: Quick Knowledge Check

**Duration:** 5 minutes

**Speaker notes:** Use these questions to gauge understanding and address any confusion. Don't make this stressful - it's about identifying gaps, not testing knowledge. Encourage discussion of answers. Use incorrect answers as teaching moments to reinforce key concepts.

**In-class prompt:** Discuss answers with someone nearby before we review together.

1. **What's the main difference between an LLM and traditional autocomplete?**
2. **Why might an LLM give a confident but wrong answer?**
3. **What makes an AI system "agentic" rather than just conversational?**
4. **Name one ethical concern when using LLMs in real applications.**
5. **What's one limitation of current language models?**

## Slide: Key Takeaways & Recap

**Duration:** 3 minutes

**Speaker notes:** Emphasize that this is just the beginning. The field is moving incredibly fast, but the fundamentals we covered today will remain relevant. Encourage continued learning and experimentation. Point out that many breakthrough applications started with simple experiments like what we built today.

**In-class prompt:** What's one thing you want to try building with AI after today?

- LLMs are sophisticated pattern matching systems trained on vast text
- AI agents combine language understanding with the ability to take actions
- Context and retrieval make LLMs much more accurate and useful
- Always consider safety, bias, and limitations when deploying AI
- The building blocks we learned today power billion-dollar AI products

## Slide: Questions & Next Steps

**Duration:** 2 minutes

**Speaker notes:** Take any remaining questions. Provide resources for continued learning: online courses, documentation, practice projects. Emphasize that the best way to learn AI is by building things. Suggest starting with simple projects and gradually increasing complexity.

**In-class prompt:** What's your biggest remaining question about LLMs or AI agents?

**Resources for continued learning:**
- Ollama documentation for local LLM experiments
- OpenAI API docs for cloud-based development  
- Hugging Face for pre-trained models and datasets
- LangChain for building AI applications
- FastAPI for creating AI-powered web services

**Code Labs:**
- `lab1_chat.py` - Your First LLM Chat
- `lab2_qa.py` - Smart Question Answerer  
- `lab3_agent.py` - Simple AI Agent
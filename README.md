LLM Workshop Setup Instructions

This workshop requires Python 3.10+ and the following setup:

STEP 1: Install Ollama
1. Download Ollama from https://ollama.ai
2. Install for your operating system
3. Open terminal/command prompt
4. Run: ollama pull llama3.2:1b

STEP 2: Install Python Dependencies
pip install ollama-python requests

STEP 3: Test Installation
Run any of the lab files to test:
python lab1_chat.py

FALLBACK MODE:
If Ollama installation fails, all labs will automatically run in "mock mode" 
with simplified functionality to demonstrate the concepts.

LAB FILES:
- lab1_chat.py - Basic LLM chat interface
- lab2_qa.py - Context-based question answering
- lab3_agent.py - AI agent with tools

TROUBLESHOOTING:
- If "Import ollama could not be resolved" error appears, the package isn't installed
- If Ollama service isn't running, start it with: ollama serve
- All code includes fallback modes that work without external dependencies

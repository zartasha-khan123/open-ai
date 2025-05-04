🤖 Zartasha Agent – AI Chat Assistant (Streamlit + OpenRouter + DeepSeek)
Welcome to Zartasha Agent, a sleek, fully functional AI-powered chatbot built with Streamlit and OpenRouter, using the DeepSeek LLM via the agents library.

This app allows users to ask natural language questions, receive intelligent responses, customize tones, pin useful answers, and view chat history—all in a clean web UI.

🚀 Features
🔐 Secure API integration via .env or Streamlit secrets

🎛 Customizable chat mode and response tone

💬 Predefined suggested questions

📌 Ability to pin favorite answers

📜 Chat history management with clear formatting

✅ Built-in error handling and spinner feedback

⚡ Powered by OpenRouter + DeepSeek Chat v3

🧠 Tech Stack
Tool / Library	Purpose
streamlit	Frontend interface
python-dotenv	Loads local .env files securely
agents	Agent-based abstraction for LLMs
Runner	Handles the execution of prompt sessions
AsyncOpenAI	Async client wrapper for OpenRouter API
DeepSeek	Underlying LLM (via OpenRouter)
OpenRouter API	Backend LLM service for response generation

📁 Folder & File Structure
graphql
Copy
Edit
📦 your-project/
├── .env                 # Your API key (local only, not committed)
├── main.py              # Main Streamlit app
├── requirements.txt     # All Python dependencies
├── README.md            # This documentation
└── .streamlit/
    └── secrets.toml     # For deployment API key
🔐 Environment Setup
1. Create a .env file:
env
Copy
Edit
OPENROUTER_API_KEY=your-api-key-here
2. Or, for Streamlit Cloud:
Add secrets.toml in .streamlit/ folder:

toml
Copy
Edit
# .streamlit/secrets.toml
OPENROUTER_API_KEY = "your-api-key-here"
⚠️ Never commit .env or .toml files to GitHub with real keys!

🧪 How to Run Locally
bash
Copy
Edit
# 1. Clone the repo
git clone https://github.com/yourusername/zartasha-agent.git
cd zartasha-agent

# 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run main.py
🖼️ Screenshots
(You can insert images here showing the UI, cards, history, etc.)

✨ Customize
You can easily extend the assistant with different models, tones, or use your own instructions in this part:

python
Copy
Edit
instructions=f'You are a helpful assistant who answers in a {tone.lower()} tone.'
📌 Credit
Powered by OpenRouter

Uses DeepSeek Chat v3

Inspired by Streamlit's chatbot design patterns

🛡️ License
This project is licensed under the MIT License. You may freely use and modify it.

# Gemini AI Chatbot 🤖

A sophisticated Python chatbot powered by Google's Gemini AI with robust error handling, conversation tracking, and seamless user interaction.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![AI](https://img.shields.io/badge/AI-Gemini_2.5_Flash-orange.svg)
![GitHub](https://img.shields.io/badge/Status-Production_Ready-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🗣️ **Natural Conversations** - Chat seamlessly with Google's Gemini AI
- 🔄 **Smart Retry Logic** - 3 automatic retries on network failures
- 📊 **Conversation Analytics** - Track your chat exchange count
- 🛡️ **Robust Error Handling** - Graceful failure management
- 🔒 **Secure Configuration** - Environment-based API key management
- 🚀 **Production Ready** - Reliable and user-friendly interface
- ⚡ **Fast Responses** - Powered by Gemini 2.5 Flash model

## 🎯 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google AI Studio API key ([Get it here](https://aistudio.google.com/))

### Installation

```bash
# Clone the repository
git clone https://github.com/Talhaarif326/ai-chatbot-python.git

# Navigate to project directory
cd ai-chatbot-python

# Install dependencies
pip install -r requirements.txt

# Setup environment configuration
cp .env.example .env
```

Usage
````
python chatbot.py
````
Example Interaction:
````
You: Explain quantum computing in simple terms
*************************
Gemini: Quantum computing uses qubits that can exist in multiple states...
*************************
You: quit
Gemini: Goodbye.
We had 3 Exchanges.
````
**🛠️ Technical Details**
**Project Structure**
text
ai-chatbot-python/
├── chatbot.py          # Main application
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
├── .env.example       # Environment template
└── README.md          # Project documentation

**Dependencies**
google-generativeai - Google's Gemini AI client library

python-dotenv - Environment variables management

**Error Handling Features**
3 retry attempts on network failures

3-second delays between retries

Clear user feedback during recovery

Graceful exit on permanent failures

**🔧 API Configuration**
The chatbot uses Google's Gemini 2.5 Flash model for optimal performance:

python
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=input
)
**💡 Usage Examples**
Learning & Education - Ask complex questions

Code Assistance - Get programming help

Content Creation - Generate ideas and content

Research - Quick information lookup

Casual Conversation - Natural AI interactions

**🐛 Troubleshooting**
Common Issues
API Key Error: Verify your key in .env file

Network Issues: Chatbot automatically retries 3 times

Rate Limits: Stay within Google's free tier limits

Module Errors: Run pip install -r requirements.txt

Debug Mode
The chatbot provides detailed error messages and retry status for easy debugging.

**🤝 Contributing**
Contributions are welcome! Please feel free to submit a Pull Request.

**Fork the project**

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


**👨‍💻 Developer**
Talha Arif

GitHub: @Talhaarif326

Project: AI Chatbot Python

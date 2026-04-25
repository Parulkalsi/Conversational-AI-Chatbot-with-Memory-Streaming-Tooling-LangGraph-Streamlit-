# Conversational-AI-Chatbot-with-Memory-Streaming-Tooling-LangGraph-Streamlit-
This project is an advanced AI-powered conversational chatbot built using LangGraph, designed to simulate real-world assistant behavior with Persistent memory, Streaming responses, Conversation resuming and Tools integration.

✅ Persistent memory (multi-thread conversations)
⚡ Streaming responses (real-time AI typing)
🔄 Conversation resuming
🔧 Tool integration (Web Search + Stock Data)

Unlike basic chatbots, this system maintains context across sessions, allowing users to revisit and continue past conversations seamlessly.

🚀 Key Highlights
🧵 Thread-based memory system (multi-chat support)
💾 Persistent storage using SQLite
⚡ Streaming responses (token-by-token output)
🔄 Resume previous conversations anytime
🔧 Tool-enabled AI agent
Web Search (DuckDuckGo)
Stock Price API

🎯 Built using LangGraph agent workflows

🧠 How It Works
User Input (Streamlit UI)
        ↓
LangGraph Agent (StateGraph)
        ↓
LLM (with Tool Binding)
        ↓
Tool Execution (if required)
        ↓
Response streamed back to UI
        ↓
Stored in SQLite (thread memory)

⚙️ Tech Stack
LLM Framework: LangGraph, LangChain, OpenAI

Frontend: Streamlit
Memory Layer: SQLite (via LangGraph Checkpointer)

Tools:
DuckDuckGo Search
Alpha Vantage Stock API
Streaming: LangGraph .stream() API
Session Handling: Streamlit session state

✨ Features Breakdown
🧵 Multi-Thread Conversations
Each chat is assigned a unique thread ID
Users can switch between past conversations
Chat history is preserved and reloadable

💾 Persistent Memory (SQLite)
Uses SqliteSaver from LangGraph
Stores conversation states automatically
Enables long-term context retention

⚡ Streaming Responses
AI responses are streamed in real-time
Improves UX by mimicking typing behavior

🔄 Conversation Resume
Sidebar shows all previous threads
Click any thread → reload full conversation

🔧 Tool Calling (Agentic Behavior)
🌐 Web Search
Fetches real-time information using DuckDuckGo

📈 Stock Price Tool
Retrieves live stock data using Alpha Vantage API
📂 Project Structure
├── langraph_chatbot.py   # LangGraph agent + memory logic
├── streamlit_app.py      # Streamlit UI
├── chatbot.db            # SQLite database (auto-created)
├── requirements.txt
└── .env
🖥️ User Interface

Sidebar:
➕ Start new chat
🧵 View previous conversations
🔄 Resume any thread

Main Chat:
💬 Interactive chat UI
⚡ Streaming AI responses
🔌 Core Components

1. LangGraph Agent
Uses StateGraph
Supports conditional tool execution
Maintains message state

3. Memory Layer
checkpointer = SqliteSaver(conn=conn)
Automatically stores conversation history
Enables retrieval using thread IDs

5. Streaming Logic
chatbot.stream(..., stream_mode='messages')
Streams only AI responses
Improves real-time interaction

🔐 Environment Setup

Create a .env file:

OPENAI_API_KEY=your_api_key_here
▶️ How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run Streamlit app
streamlit run streamlit_app.py

4. Open in browser
http://localhost:8501
🧪 Example Use Cases
“What’s the latest news about AI?”
“Get Tesla stock price”
“Continue my previous conversation”

🎯 What I Learned
Building stateful AI systems using LangGraph
Implementing persistent memory with SQLite
Designing multi-thread conversation systems
Streaming responses for better UX
Creating agentic workflows with tool execution

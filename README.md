<div align="center">

# 🧠 Autonomous Research Assistant

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=667EEA&center=true&vCenter=true&width=600&lines=LangGraph+%7C+Groq+%7C+LLaMA+3.3+70B;Real-time+Web+Search+%7C+Wikipedia;Bengali+%F0%9F%87%A7%F0%9F%87%A9+%26+English+%F0%9F%87%AC%F0%9F%87%A7+Support;PDF+%26+Document+Analysis)](https://huggingface.co/spaces/mahabub-unlocked/QueryMind-AI)

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-ReAct_Agent-FF6B6B?style=for-the-badge)](https://langchain-ai.github.io/langgraph/)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F54E42?style=for-the-badge)](https://groq.com)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Deployed-FFD21E?style=for-the-badge)](https://huggingface.co/spaces/mahabub-unlocked/QueryMind-AI)
[![License](https://img.shields.io/badge/License-MIT-2ecc71?style=for-the-badge)](LICENSE)

<br/>

> **এটি একটি intelligent AI research assistant যা LangGraph-এর ReAct agent framework ব্যবহার করে real-time web search, Wikipedia analysis, এবং document processing করে — বাংলা ও ইংরেজি উভয় ভাষায় বিস্তারিত উত্তর প্রদান করে।**

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-667EEA?style=for-the-badge)](https://huggingface.co/spaces/mahabub-unlocked/autonomous-research-assistant)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Usage Examples](#-usage-examples)
- [How ReAct Agent Works](#-how-react-agent-works)
- [Project Structure](#-project-structure)
- [What I Learned](#-what-i-learned)

---

## 🎯 Overview

Autonomous Research Assistant হল একটি production-ready AI application যা তিনটি powerful tool combine করে intelligent research করে:

- 🔍 **DuckDuckGo Web Search** — Real-time internet থেকে সর্বশেষ তথ্য
- 📖 **Wikipedia Analysis** — যেকোনো বিষয়ে structured academic তথ্য
- 📄 **Document Processing** — PDF ও TXT file upload করে AI-powered analysis

LangGraph-এর **ReAct (Reasoning + Acting)** framework ব্যবহার করে agent নিজেই decide করে কোন tool কখন use করবে — কোনো hardcoding নেই।

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🔍 **Web Search** | DuckDuckGo দিয়ে real-time internet search | ✅ Live |
| 📖 **Wikipedia Search** | যেকোনো বিষয়ে বিস্তারিত Wikipedia তথ্য | ✅ Live |
| 📄 **File Analysis** | PDF ও TXT file upload করে AI analysis | ✅ Live |
| 🌐 **Multilingual** | Bengali 🇧🇩 ও English 🇬🇧 response support | ✅ Live |
| ⚡ **Streaming Output** | Real-time টাইপিং effect-এ response | ✅ Live |
| 💾 **Chat History** | Conversation save ও load | ✅ Live |
| 📥 **PDF Export** | পুরো chat PDF-এ export | ✅ Live |
| 📋 **Copy Button** | যেকোনো response এক click-এ copy | ✅ Live |
| 🧠 **ReAct Agent** | Autonomous tool selection ও decision making | ✅ Live |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    USER INTERFACE                        │
│              Streamlit Chat Application                  │
│         (Bengali / English • File Upload)               │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                  REACT AGENT CORE                        │
│              LangGraph (ReAct Framework)                 │
│                                                         │
│   Thought → Action → Observation → Final Answer         │
└──────┬────────────────┬────────────────┬────────────────┘
       │                │                │
       ▼                ▼                ▼
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Web Search │ │  Wikipedia  │ │    File     │
│ DuckDuckGo  │ │    Search   │ │   Loader    │
│     🔍      │ │     📖      │ │     📄      │
└──────┬──────┘ └──────┬──────┘ └──────┬──────┘
       └────────────────┴────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│                  LLM INFERENCE                           │
│          LLaMA 3.3 70B via Groq API                     │
│         (Ultra-fast inference • 4096 tokens)            │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│               STREAMING RESPONSE                         │
│    Real-time output • History • Export • Copy           │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit 1.32 | Chat UI, file upload, sidebar |
| **AI Agent** | LangGraph (ReAct) | Autonomous reasoning & tool use |
| **LLM** | LLaMA 3.3 70B via Groq | Natural language generation |
| **Web Search** | DuckDuckGo Search | Real-time internet search |
| **Knowledge Base** | Wikipedia API | Structured academic content |
| **PDF Processing** | pypdf | Document text extraction |
| **PDF Export** | fpdf2 | Chat history export |
| **Framework** | LangChain | LLM orchestration |
| **Language** | Python 3.10+ | Core application |
| **Deployment** | Hugging Face Spaces | Cloud hosting |

---

## 🚀 Getting Started

### Prerequisites

```
Python 3.10+
Groq API Key → https://console.groq.com (Free)
```

### Installation

**1. Repository clone করো**

```bash
git clone https://github.com/mdmahabubalambishal/Autonomous-Research-Assistant.git
cd Autonomous-Research-Assistant
```

**2. Virtual environment তৈরি করো**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

**3. Dependencies install করো**

```bash
pip install -r requirements.txt
```

**4. Environment variables set করো**

`.env` file তৈরি করো:

```env
GROQ_API_KEY=your_groq_api_key_here
```

**5. App চালাও**

```bash
streamlit run app.py
```

Browser-এ যাও: `http://localhost:8501`

---

## 🧪 Usage Examples

### 🔍 Web Search
```
"২০২৫ সালে AI-এর সর্বশেষ developments কী কী?"
"Latest news about GPT-5?"
"বাংলাদেশের অর্থনীতির বর্তমান অবস্থা কী?"
```

### 📖 Wikipedia Research
```
"Artificial Intelligence-এর ইতিহাস বিস্তারিত বলো"
"Quantum Computing কীভাবে কাজ করে?"
"Machine Learning vs Deep Learning পার্থক্য কী?"
```

### 📄 Document Analysis
```
১. Sidebar-এ PDF upload করো
২. "এই document-এর মূল বিষয় কী?" — জিজ্ঞেস করো
৩. "Summarize this document in Bengali"
৪. "এই paper-এর key findings কী?"
```

---

## 🔄 How ReAct Agent Works

```
Step 1 → THOUGHT
         User query analyze করে
         কোন tool দরকার সেটা decide করে

Step 2 → ACTION
         সঠিক tool select করে execute করে
         Web Search / Wikipedia / File Analysis

Step 3 → OBSERVATION
         Tool-এর result observe করে
         Answer sufficient কিনা evaluate করে

Step 4 → FINAL ANSWER
         LLaMA 3.3 70B দিয়ে response generate করে
         Bengali বা English-এ real-time stream করে
```

---

## 📁 Project Structure

```
Autonomous-Research-Assistant/
│
├── 📄 app.py               # Streamlit UI & main application
├── 🤖 agent.py             # LangGraph ReAct agent setup
├── 🔧 tools.py             # Custom LangChain tools definition
├── 📋 requirements.txt     # Python dependencies
├── 🔒 .env                 # API keys (local only, gitignored)
├── 🚫 .gitignore           # Git ignore rules
└── 📖 README.md            # Project documentation
```

---

## 💡 What I Learned

```
✅ LangGraph ReAct Agent
   ├── Multi-step autonomous reasoning
   ├── Intelligent tool selection
   └── Stateful graph execution

✅ Tool Integration
   ├── DuckDuckGo real-time web search
   ├── Wikipedia structured data retrieval
   └── PDF/TXT file processing pipeline

✅ Streaming Response
   ├── Real-time character-by-character output
   └── Typing effect implementation in Streamlit

✅ Multilingual LLM
   ├── Bengali language support with LLaMA
   ├── Dynamic language switching
   └── Structured response formatting

✅ Production Deployment
   ├── HuggingFace Spaces configuration
   ├── Secret management (API keys)
   └── Dependency management
```

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| Web Search response | ~2-3 seconds |
| Wikipedia response | ~1-2 seconds |
| Document analysis | ~3-5 seconds |
| LLM Model | LLaMA 3.3 70B |
| Max tokens | 4096 |
| Languages | Bengali, English |

---

<div align="center">

## 👨‍💻 Author

**Md Mahabub Alam Bishal**
*AI/ML Engineer | LLM & Generative AI Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/md-mahabub-alam-bishal/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/mdmahabubalambishal)
[![HuggingFace](https://img.shields.io/badge/🤗_HuggingFace-Follow-FFD21E?style=for-the-badge)](https://huggingface.co/mahabub-unlocked)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail)](mailto:mdmahabubalambishal@gmail.com)

<br/>

## 🙏 Acknowledgements

[LangChain](https://langchain.com/) • [LangGraph](https://langchain-ai.github.io/langgraph/) • [Groq](https://groq.com/) • [DuckDuckGo](https://duckduckgo.com/) • [Wikipedia](https://wikipedia.org/) • [Streamlit](https://streamlit.io/) • [Hugging Face](https://huggingface.co/)

<br/>

---

⭐ **এই project টা useful লাগলে GitHub-এ একটা Star দাও!**

*Made with ❤️ by Mahabub Alam*

**[🚀 Live Demo](https://https://huggingface.co/spaces/mahabub-unlocked/autonomous-research-assistant)** • **[📂 GitHub](https://github.com/mdmahabubalambishal/Autonomous-Research-Assistant)**

</div>
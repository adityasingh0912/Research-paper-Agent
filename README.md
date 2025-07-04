# Agentic AI Research Workflow

A modular, agentic research pipeline using LangChain, Groq LLMs, and tool-based orchestration.  
This project automates the process of searching for academic papers, summarizing, critiquing, and compiling research reports.

---

## Features

- **Research Agent**: Finds relevant academic papers using Tavily API.
- **Summarization Agent**: Summarizes papers using LLM tools.
- **Critic Agent**: Critiques the generated summary.
- **Writer Agent**: Compiles a final markdown report.
- **RAG Pipeline**: Modular chunking, retrieval, compression, and synthesis utilities.
- **Groq LLM Integration**: Uses Groq's OpenAI-compatible API for fast, cost-effective inference.

---

## Installation


1. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```
   GROQ_API=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

---

## Usage

Run the main script:

```bash
python research.py
```

You will be prompted to enter a research topic.  
The system will search for papers, summarize, critique, and compile a markdown report.

---

## Repository Structure

```
agentic_ai/
│
├── .env                  # Environment variables (not committed)
├── requirements.txt      # Python dependencies
├── research.py           # Main entry point
│
├── agents/               # Agent tool definitions
│   ├── research_agent.py
│   ├── summarization_agent.py
│   ├── critic_agent.py
│   └── writer_agent.py
│
├── rag/                  # RAG pipeline utilities
│   ├── chunking.py
│   ├── retrieval.py
│   ├── compression.py
│   └── synthesis.py
│
├── workflow/             # Workflow orchestration
│   └── orchestrator.py
│
└── utils/
    └── groq_llm.py       # Groq LLM utility
```

---

## Implementation Details

- **Agents**: Each agent is a LangChain tool-based agent, initialized with a Groq LLM and a set of tools.
- **LLM Integration**: The `utils/groq_llm.py` provides a helper to instantiate a `ChatOpenAI` object pointed at Groq's API endpoint.
- **Research Tool**: Uses Tavily API to fetch academic papers. (You must provide your own API key.)
- **Workflow**: The orchestrator sequentially runs each agent, passing outputs as inputs to the next stage.
- **RAG Utilities**: Modular scripts for chunking, retrieval, compression, and synthesis, ready for extension.

---

## Design Decisions & Trade-offs

- **LangChain Agents**: Chosen for flexibility and easy tool integration.
- **Groq LLM**: Used for speed and cost; compatible with OpenAI API, so minimal code changes are needed.
- **Separation of Concerns**: Each agent/tool is modular, making it easy to swap or extend.
- **Simplicity vs. Extensibility**: The current pipeline is linear for clarity, but can be extended to more complex workflows (e.g., parallel summarization, multi-agent collaboration).
- **Error Handling**: Basic error handling is included; production use should add retries, logging, and more robust validation.

---

## Extensions & Improvements

Given more time, the following improvements are recommended:

- **Better Error Handling**: Add retries, logging, and user-friendly error messages.
- **Async Support**: Make the workflow fully asynchronous for speed.
- **UI/Frontend**: Build a web interface for interactive research.
- **Advanced RAG**: Integrate vector search, semantic chunking, and more sophisticated synthesis.
- **Agent Memory**: Add persistent memory or context windows for agents.
- **Evaluation**: Add automated evaluation of summaries and critiques.
- **Unit Tests**: Add tests for all modules and workflows.
- **Dockerization**: Provide a Dockerfile for easy deployment.

---



## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)
- [Tavily API](https://docs.tavily.com/)

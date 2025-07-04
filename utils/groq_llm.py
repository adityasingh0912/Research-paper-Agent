import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_groq_llm(model="llama-3.3-70b-versatile"):
    return ChatOpenAI(
        model=model,
        openai_api_key=os.getenv("GROQ_API"),
        openai_api_base="https://api.groq.com/openai/v1",
        temperature=0.1  # <-- Makes output more deterministic
        )
        
    
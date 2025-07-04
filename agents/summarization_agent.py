from langchain.tools import tool

@tool
def summarize_papers(papers: str) -> str:
    """
    Summarize the provided research papers.
    """
    return f"Summarize these papers:\n{papers}"

def get_summarization_tools():
    return [summarize_papers]

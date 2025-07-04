from langchain.tools import tool

@tool
def critique_summary(summary: str) -> str:
    """
    Critique the provided summary.
    """
    return f"Critique this summary:\n{summary}"

def get_critic_tools():
    return [critique_summary]

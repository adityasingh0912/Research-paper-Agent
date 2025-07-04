from langchain.tools import tool

@tool
def compile_report(input: str) -> str:
    """
    Compile a report from a string containing papers, summary, and critique.
    """
    return f"# Research Report\n\n{input}"

def get_writer_tools():
    return [compile_report]

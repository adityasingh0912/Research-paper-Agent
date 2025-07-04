import os
import requests
from langchain.tools import tool

NUM_PAPERS = 3

@tool
def search_papers(query: str) -> str:
    """
    Action: search_papers
    Action Input: A research topic as a string.
    Returns: A numbered list of up to NUM_PAPERS research paper titles and URLs.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    url = "https://api.tavily.com/search"
    json_data = {
        "query": query,
        "category": "research_papers",
        "num_results": NUM_PAPERS
    }
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(url, json=json_data, headers=headers)  # <-- POST, not GET!
    if response.status_code != 200:
        return f"Error fetching papers: {response.text}"
    results = response.json().get("results", [])
    if not results:
        return "No papers found."
    return "\n".join([f"{i+1}. {r['title']} ({r.get('year', 'n/a')}): {r['url']}" for i, r in enumerate(results)])

def get_research_tools():
    return [search_papers]

def chunk_papers(papers: str) -> list:
    # Split papers into sections or fixed-size chunks
    return [papers[i:i+1000] for i in range(0, len(papers), 1000)]

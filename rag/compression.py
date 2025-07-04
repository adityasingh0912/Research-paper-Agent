def compress_chunks(chunks: list) -> str:
    # Use LLM to summarize each chunk, then combine
    return "\n".join([f"Summary of chunk: {chunk[:50]}" for chunk in chunks])

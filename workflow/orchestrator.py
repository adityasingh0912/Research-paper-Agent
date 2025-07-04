from utils.groq_llm import get_groq_llm
from agents.research_agent import get_research_tools
from agents.summarization_agent import get_summarization_tools
from agents.critic_agent import get_critic_tools
from agents.writer_agent import get_writer_tools
from langchain.agents import initialize_agent, AgentType

def run_workflow(query: str):
    llm = get_groq_llm()

    # Research Agent
    research_agent = initialize_agent(
        get_research_tools(),
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    papers = research_agent.invoke(query)

    # Summarization Agent
    summarization_agent = initialize_agent(
        get_summarization_tools(),
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    summary = summarization_agent.invoke(papers)

    # Critic Agent
    critic_agent = initialize_agent(
        get_critic_tools(),
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    critique = critic_agent.invoke(summary)

    # Writer Agent
    writer_agent = initialize_agent(
        get_writer_tools(),
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    writer_input = f"""Papers:
    {papers}

    Summary:
    {summary}

    Critique:
    {critique}
    """
    report = writer_agent.invoke({"input": writer_input})

    return report

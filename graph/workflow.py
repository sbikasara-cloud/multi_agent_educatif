from state import AgentState
from agents.supervisor import route_query
from agents.rag_agent import run_rag_agent
from agents.pedagogique import run_pedagogique_agent
from tools.retriever_tools import build_retriever

def process_query(query: str) -> str:
    agent = route_query(query)

    if agent == "pedagogique":
        return run_pedagogique_agent(query)

    if agent == "correction":
        return "Correction non encore implémentée."

    retriever = build_retriever()
    docs = retriever.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return run_rag_agent(query, context)
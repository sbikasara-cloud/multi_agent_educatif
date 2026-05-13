from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    query: str
    retrieved_context: str
    agent_response: str
    human_approved: bool
    next_agent: str
    corpus_used: str
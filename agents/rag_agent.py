from pathlib import Path
from config.llm_config import get_llm

PROMPT_PATH = Path("prompts/rag_agent.txt")

def run_rag_agent(query: str, context: str) -> str:
    llm = get_llm(temperature=0.2)
    prompt = PROMPT_PATH.read_text(encoding="utf-8").format(query=query, context=context)
    return llm.invoke(prompt).content
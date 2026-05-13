from pathlib import Path
from config.llm_config import get_llm

PROMPT_PATH = Path("prompts/supervisor.txt")

def route_query(query: str) -> str:
    llm = get_llm(temperature=0)
    prompt = PROMPT_PATH.read_text(encoding="utf-8").format(query=query)
    response = llm.invoke(prompt).content.strip().lower()

    if "pedagogique" in response:
        return "pedagogique"
    if "correction" in response:
        return "correction"
    return "rag"
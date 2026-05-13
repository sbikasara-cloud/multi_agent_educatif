from pathlib import Path
from config.llm_config import get_llm

PROMPT_PATH = Path("prompts/pedagogique.txt")

def run_pedagogique_agent(query: str) -> str:
    llm = get_llm(temperature=0.4)
    prompt = PROMPT_PATH.read_text(encoding="utf-8").format(query=query)
    return llm.invoke(prompt).content
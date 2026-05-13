from langchain_ollama import ChatOllama, OllamaEmbeddings

def get_llm(temperature: float = 0) -> ChatOllama:
    return ChatOllama(
        model="llama3.2:1b",
        temperature=temperature,
        num_ctx=1024
    )

def get_embeddings() -> OllamaEmbeddings:
    return OllamaEmbeddings(model="llama3.2:1b")
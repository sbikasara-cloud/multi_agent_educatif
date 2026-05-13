from graph.workflow import process_query

if __name__ == "__main__":
    print("Assistant éducatif multi-agent prêt.")
    while True:
        query = input("\nVotre question : ").strip()
        if query.lower() in {"exit", "quit", "stop"}:
            break
        response = process_query(query)
        print("\nRéponse :\n", response)
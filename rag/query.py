import json

def retrieve(query):
    with open("index.json", "r", encoding="utf-8") as f:
        docs = json.load(f)

    query = query.lower()
    relevant = []

    for doc in docs:
        if any(word in doc["content"].lower() for word in query.split()):
            relevant.append(doc["content"])

    return relevant if relevant else [docs[0]["content"]]

def generate_answer(query, context):
    return f"""
Question:
{query}

Answer (simulated RAG response):
Based on the retrieved context, {context[:500]}...
"""

def main():
    query = input("Ask a question: ")
    context = "\n\n".join(retrieve(query))
    answer = generate_answer(query, context)

    print("\n--- Answer ---\n")
    print(answer)

if __name__ == "__main__":
    main()

import json
from pathlib import Path

BASE_PATH = Path("../output")

def load_documents():
    docs = []

    docs.append({
        "source": "summary",
        "content": (BASE_PATH / "summary.md").read_text(encoding="utf-8")
    })

    docs.append({
        "source": "entities",
        "content": (BASE_PATH / "entities.json").read_text(encoding="utf-8")
    })

    return docs

def main():
    documents = load_documents()

    with open("index.json", "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print("✅ RAG index (non-embedding) built successfully")

if __name__ == "__main__":
    main()

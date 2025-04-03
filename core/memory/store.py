"""
E.V.A. Memory Store (Prototype)
- Stores memories as JSON entries
- Enables semantic retrieval for recall
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "eva_memory.json"


def save_memory(entry: dict):
    """Append a memory entry to EVA's memory file."""
    data = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def retrieve_relevant_memories(query: str, max_results: int = 3) -> list:
    """Retrieve recent relevant memories based on keyword match."""
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        memories = json.load(f)

    # Simple filter by keyword match
    filtered = [m for m in memories if query.lower() in m.get("input", "").lower()]
    return filtered[-max_results:] if filtered else memories[-max_results:]


def test_memory():
    test_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": "Test input",
        "output": "Test output",
        "reflection": "Thinking about testing.",
        "tags": ["test"]
    }
    save_memory(test_entry)
    print("Saved.")
    print("Relevant Memories:", retrieve_relevant_memories("test"))


if __name__ == "__main__":
    test_memory()

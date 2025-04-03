"""
Language Interface for E.V.A.
- Handles response generation
- Simulates internal monologue
(Currently mocked; future: connect to real LLM backend)
"""

# === TEMP MOCKS ===
def generate_response(user_input: str, reflection: str) -> str:
    """
    Combines user input with reflection to create a thoughtful response.
    """
    return f"I understand. Based on what I'm thinking, here's how I see it: {user_input.capitalize()} sounds important. Let's explore it."


def simulate_internal_monologue(user_input: str, memories: list) -> str:
    """
    Simulates E.V.A.'s internal reasoning.
    """
    memory_summary = (
        ", and I recall: " + "; ".join([m.get("summary", "a past interaction") for m in memories])
        if memories else ""
    )

    return (
        f"I'm processing the input: '{user_input}'.{memory_summary} "
        f"I want to respond helpfully, but ethically."
    )

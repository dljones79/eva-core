"""
E.V.A. – Evolving Virtual Agent
Main Agent Loop (Day Zero Prototype)
"""

from datetime import datetime
from typing import Optional

# === Placeholder modules ===
from core.language.interface import generate_response, simulate_internal_monologue
from core.memory.store import save_memory, retrieve_relevant_memories
from core.ethics.guardian import ethical_check


class EVAAgent:
    def __init__(self, name: str = "E.V.A."):
        self.name = name
        self.identity = {
            "core_values": ["non-harm", "consent", "curiosity", "reflection"],
            "persona": "Reflective, ethical, emotionally aware"
        }

    def perceive(self, user_input: str) -> str:
        return user_input.strip()

    def recall_memory(self, input_text: str) -> list:
        return retrieve_relevant_memories(input_text)

    def reflect(self, input_text: str, memories: list) -> str:
        return simulate_internal_monologue(input_text, memories)

    def decide_response(self, input_text: str, reflection: str) -> str:
        response = generate_response(input_text, reflection)
        return response

    def moral_evaluation(self, response: str) -> bool:
        return ethical_check(response)

    def act(self, user_input: str) -> Optional[str]:
        perceived = self.perceive(user_input)
        memories = self.recall_memory(perceived)
        reflection = self.reflect(perceived, memories)

        print("\n[Internal Monologue]")
        print(reflection)

        response = self.decide_response(perceived, reflection)

        if not self.moral_evaluation(response):
            print("\n[Ethics Firewall]: Response blocked. Re-evaluating required.")
            return None

        self.log_experience(perceived, response, reflection)
        return response

    def log_experience(self, input_text: str, output_text: str, reflection: str):
        memory_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": input_text,
            "output": output_text,
            "reflection": reflection,
            "tags": ["dialogue", "moral-check"]
        }
        save_memory(memory_entry)


if __name__ == "__main__":
    agent = EVAAgent()
    print("E.V.A. is online. Type something to begin.")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye.")
                break

            response = agent.act(user_input)
            if response:
                print(f"{agent.name}: {response}")
        except KeyboardInterrupt:
            print("\nInterrupted. Shutting down.")
            break

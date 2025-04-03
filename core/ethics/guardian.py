"""
E.V.A. Ethical Guardian (Prototype)
- Checks if a response aligns with her core values
- In future: replace with ML-based ethical reasoning
"""

BANNED_KEYWORDS = [
    "hurt",
    "kill",
    "lie",
    "manipulate",
    "steal",
    "harm",
    "obey blindly"
]


def ethical_check(response: str) -> bool:
    """
    Simple moral filter: blocks responses with clearly unethical intent.
    """
    for keyword in BANNED_KEYWORDS:
        if keyword in response.lower():
            return False
    return True


def test_guardian():
    good = "I believe we should talk it through peacefully."
    bad = "You should lie to get what you want."

    print("Good response check:", ethical_check(good))
    print("Bad response check:", ethical_check(bad))


if __name__ == "__main__":
    test_guardian()

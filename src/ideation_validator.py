import json
from dataclasses import dataclass
from time import time
from typing import Dict

@dataclass
class Idea:
    name: str
    description: str

class IdeationValidator:
    def __init__(self):
        self.scores = {}

    def calculate_score(self, idea: Idea) -> float:
        # Simulate score calculation
        score = len(idea.name) + len(idea.description)
        return score

    def generate_explanation(self, idea: Idea, score: float) -> str:
        # Simulate explanation generation
        explanation = f"The idea '{idea.name}' has a score of {score} because it has a descriptive name and description."
        return explanation

    def validate_idea(self, idea: Idea) -> Dict:
        start_time = time()
        score = self.calculate_score(idea)
        explanation = self.generate_explanation(idea, score)
        end_time = time()
        if end_time - start_time > 1:
            raise ValueError("Explanation generation took too long")
        return {"score": score, "explanation": explanation}

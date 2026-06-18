import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    name: str
    description: str
    feasibility: float
    potential_revenue: float

class IdeationValidator:
    def __init__(self):
        self.ideas = []

    def generate_ideas(self, text: str) -> List[Idea]:
        # Simple idea generation logic
        ideas = []
        for word in text.split():
            idea = Idea(word, f"A software tool for {word}", 0.5, 1000.0)
            ideas.append(idea)
        return ideas

    def validate_idea(self, idea: Idea) -> bool:
        # Simple validation logic
        return idea.feasibility > 0.3 and idea.potential_revenue > 500.0

    def get_validated_ideas(self, text: str) -> List[Idea]:
        ideas = self.generate_ideas(text)
        validated_ideas = [idea for idea in ideas if self.validate_idea(idea)]
        return validated_ideas

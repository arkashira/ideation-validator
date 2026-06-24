import json
from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    name: str
    revenue_potential: float
    validation_score: float

class IdeationValidator:
    def __init__(self):
        self.ideas = []

    def add_idea(self, idea: Idea):
        self.ideas.append(idea)

    def prioritize_roadmap(self, sort_by: str = 'revenue_potential'):
        if sort_by == 'revenue_potential':
            return sorted(self.ideas, key=lambda x: x.revenue_potential, reverse=True)
        elif sort_by == 'validation_score':
            return sorted(self.ideas, key=lambda x: x.validation_score, reverse=True)
        else:
            raise ValueError('Invalid sort_by parameter')

    def get_roadmap(self, sort_by: str = 'revenue_potential'):
        return self.prioritize_roadmap(sort_by)

    def estimate_revenue(self, idea: Idea):
        return idea.revenue_potential

    def validate_idea(self, idea: Idea):
        return idea.validation_score

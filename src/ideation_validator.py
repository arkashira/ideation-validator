import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List

@dataclass
class Idea:
    name: str
    monthly_search_volume: int
    google_trends_score: int
    competing_products: int
    trend_graph: List[int]

class IdeationValidator:
    def __init__(self, ideas: List[Idea]):
        self.ideas = ideas

    def get_validation_metrics(self, idea_name: str) -> Dict:
        for idea in self.ideas:
            if idea.name == idea_name:
                return {
                    "monthly_search_volume": idea.monthly_search_volume,
                    "google_trends_score": idea.google_trends_score,
                    "competing_products": idea.competing_products,
                    "trend_graph": idea.trend_graph,
                }
        return {"error": "Idea not found"}

    def refresh_data(self):
        # Simulate data refresh
        for idea in self.ideas:
            idea.monthly_search_volume += 1
            idea.google_trends_score += 1
            idea.competing_products += 1
            idea.trend_graph.append(1)

    def get_credits(self, idea_name: str) -> Dict:
        for idea in self.ideas:
            if idea.name == idea_name:
                return {
                    "monthly_search_volume": "Google Trends",
                    "google_trends_score": "Google Trends",
                    "competing_products": "Product Hunt",
                    "trend_graph": "Google Trends",
                }
        return {"error": "Idea not found"}

def load_ideas() -> List[Idea]:
    # Simulate loading ideas from a database
    ideas = [
        Idea("Idea 1", 100, 50, 10, [1, 2, 3]),
        Idea("Idea 2", 200, 60, 20, [4, 5, 6]),
    ]
    return ideas

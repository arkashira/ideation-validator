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
        self.data_sources = {
            "monthly_search_volume": "Google Trends",
            "google_trends_score": "Google Trends",
            "competing_products": "Product Hunt",
            "trend_graph": "Google Trends"
        }

    def get_validation_metrics(self, idea: Idea):
        metrics = {
            "monthly_search_volume": idea.monthly_search_volume,
            "google_trends_score": idea.google_trends_score,
            "competing_products": idea.competing_products,
            "trend_graph": idea.trend_graph
        }
        return metrics

    def refresh_data(self):
        # Simulate data refresh
        for idea in self.ideas:
            idea.monthly_search_volume += 1
            idea.google_trends_score += 1
            idea.competing_products += 1
            idea.trend_graph.append(1)

    def get_data_sources(self):
        return self.data_sources

def load_ideas_from_json(json_data: str) -> List[Idea]:
    ideas = []
    data = json.loads(json_data)
    for idea_data in data:
        idea = Idea(
            name=idea_data["name"],
            monthly_search_volume=idea_data["monthly_search_volume"],
            google_trends_score=idea_data["google_trends_score"],
            competing_products=idea_data["competing_products"],
            trend_graph=idea_data["trend_graph"]
        )
        ideas.append(idea)
    return ideas

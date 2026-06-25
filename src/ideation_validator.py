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
            "monthly_search_volume": "Google Keyword Planner",
            "google_trends_score": "Google Trends",
            "competing_products": "Product Hunt",
            "trend_graph": "Google Trends"
        }

    def get_validation_metrics(self, idea: Idea) -> Dict[str, str]:
        metrics = {
            "monthly_search_volume": str(idea.monthly_search_volume),
            "google_trends_score": str(idea.google_trends_score),
            "competing_products": str(idea.competing_products),
            "trend_graph": str(idea.trend_graph)
        }
        return metrics

    def refresh_data(self) -> None:
        # Simulate data refresh
        for idea in self.ideas:
            idea.monthly_search_volume += 1
            idea.google_trends_score += 1
            idea.competing_products += 1
            idea.trend_graph.append(1)

    def get_data_sources(self) -> Dict[str, str]:
        return self.data_sources

    def get_idea_list(self) -> List[Idea]:
        return self.ideas

def load_ideas() -> List[Idea]:
    ideas = [
        Idea("Idea 1", 100, 50, 10, [1, 2, 3]),
        Idea("Idea 2", 200, 60, 20, [4, 5, 6]),
        Idea("Idea 3", 300, 70, 30, [7, 8, 9])
    ]
    return ideas

def main() -> None:
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    print(validator.get_validation_metrics(ideas[0]))
    validator.refresh_data()
    print(validator.get_data_sources())
    print(validator.get_idea_list())

if __name__ == "__main__":
    main()

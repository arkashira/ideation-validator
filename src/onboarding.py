import json
from dataclasses import dataclass
from typing import List

@dataclass
class OnboardingTour:
    steps: List[str]

class IdeationValidator:
    def __init__(self):
        self.tour = OnboardingTour([
            "Highlight keyword input",
            "Highlight tag filter",
            "Highlight validation score"
        ])
        self.settings = {
            "tour_skipped": False,
            "tour_replayed": False
        }

    def start_tour(self):
        if self.settings["tour_skipped"]:
            return "Tour skipped"
        for step in self.tour.steps:
            print(step)
        return "Tour completed"

    def skip_tour(self):
        self.settings["tour_skipped"] = True
        return "Tour skipped"

    def replay_tour(self):
        self.settings["tour_skipped"] = False  # Reset tour_skipped to allow replay
        self.settings["tour_replayed"] = True
        return self.start_tour()

    def get_settings(self):
        return self.settings

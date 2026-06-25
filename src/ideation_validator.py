import argparse
import json
import random
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Idea:
    title: str
    description: str

class IdeationValidator:
    def __init__(self):
        self.session = []

    def generate_ideas(self, niche: str) -> List[Idea]:
        keywords = set(niche.lower().split())
        ideas = [
            {"title": "Remote Work Tracker", "description": "A tool to track remote work hours."},
            {"title": "Fitness Planner", "description": "An app to plan daily fitness routines."},
            {"title": "Remote Team Chat", "description": "A chat platform for remote teams."},
            {"title": "Fitness Tracker", "description": "A tracker for fitness goals and progress."},
            {"title": "Work-Life Balance App", "description": "An app to balance work and personal life."},
            {"title": "Fitness Challenge", "description": "A challenge-based fitness program."},
            {"title": "Remote Collaboration Tool", "description": "A tool for remote collaboration."},
            {"title": "Fitness Journal", "description": "A journal to log fitness activities."},
            {"title": "Remote Work Calendar", "description": "A calendar for remote work schedules."},
            {"title": "Fitness Community", "description": "A community for fitness enthusiasts."}
        ]
        
        filtered_ideas = [idea for idea in ideas if any(keyword in idea['title'].lower() or keyword in idea['description'].lower() for keyword in keywords)]
        unique_ideas = []
        titles = set()
        
        for idea in filtered_ideas:
            if idea['title'] not in titles:
                unique_ideas.append(Idea(idea['title'], idea['description']))
                titles.add(idea['title'])
                
        return random.sample(unique_ideas, min(len(unique_ideas), 5))

    def store_ideas(self, ideas: List[Idea]):
        self.session.extend([{"title": idea.title, "description": idea.description} for idea in ideas])

def main():
    parser = argparse.ArgumentParser(description="Generate AI-generated software-tool ideas.")
    parser.add_argument("niche", type=str, help="The niche for generating ideas.")
    args = parser.parse_args()

    ideation_validator = IdeationValidator()
    ideas = ideation_validator.generate_ideas(args.niche)
    ideation_validator.store_ideas(ideas)

    print(json.dumps([{"title": idea.title, "description": idea.description} for idea in ideas], indent=2))

if __name__ == "__main__":
    main()

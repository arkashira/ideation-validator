import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class IdeaRequest:
    timestamp: str
    keyword: str
    tags: List[str]
    user_id: int

class IdeaValidator:
    def __init__(self):
        self.ideas = []

    def log_idea(self, keyword: str, tags: List[str], user_id: int):
        idea = IdeaRequest(
            timestamp=datetime.now().isoformat(),
            keyword=keyword,
            tags=tags,
            user_id=user_id
        )
        self.ideas.append(idea)

    def get_ideas(self):
        return self.ideas

    def filter_ideas_by_retention_policy(self, retention_policy: int):
        filtered_ideas = []
        for idea in self.ideas:
            idea_date = datetime.fromisoformat(idea.timestamp)
            if (datetime.now() - idea_date).days <= retention_policy * 365:
                filtered_ideas.append(idea)
        return filtered_ideas

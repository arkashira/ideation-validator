from dataclasses import dataclass
from typing import List

@dataclass
class Idea:
    id: int
    tags: List[str]

class IdeaGenerator:
    def __init__(self, ideas: List[Idea]):
        self.ideas = ideas

    def filter_by_tags(self, tags: List[str]) -> List[Idea]:
        if len(tags) > 3:
            raise ValueError("Cannot filter by more than 3 tags")
        return [idea for idea in self.ideas if any(tag in idea.tags for tag in tags)]

    def get_tags(self) -> List[str]:
        all_tags = set()
        for idea in self.ideas:
            all_tags.update(idea.tags)
        return list(all_tags)

    def main(self):
        ideas = [
            Idea(1, ["tech", "software"]),
            Idea(2, ["fashion", "design"]),
            Idea(3, ["tech", "hardware"]),
        ]
        generator = IdeaGenerator(ideas)
        tags = ["tech"]
        filtered_ideas = generator.filter_by_tags(tags)
        print([idea.id for idea in filtered_ideas])

if __name__ == "__main__":
    IdeaGenerator([]).main()

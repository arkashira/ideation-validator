from ideation_validator import Idea, IdeaGenerator
import pytest

def test_filter_by_tags():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = ["tech"]
    filtered_ideas = generator.filter_by_tags(tags)
    assert len(filtered_ideas) == 2
    assert filtered_ideas[0].id == 1
    assert filtered_ideas[1].id == 3

def test_filter_by_tags_empty():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = []
    filtered_ideas = generator.filter_by_tags(tags)
    assert len(filtered_ideas) == 0

def test_get_tags():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = generator.get_tags()
    assert len(tags) == 5
    assert "tech" in tags
    assert "software" in tags
    assert "fashion" in tags
    assert "design" in tags
    assert "hardware" in tags

def test_filter_by_tags_multiple():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = ["tech", "fashion"]
    filtered_ideas = generator.filter_by_tags(tags)
    assert len(filtered_ideas) == 3
    assert filtered_ideas[0].id == 1
    assert filtered_ideas[1].id == 2
    assert filtered_ideas[2].id == 3

def test_filter_by_tags_more_than_three():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = ["tech", "fashion", "design", "hardware"]
    with pytest.raises(ValueError):
        generator.filter_by_tags(tags)

def test_filter_by_tags_three():
    ideas = [
        Idea(1, ["tech", "software"]),
        Idea(2, ["fashion", "design"]),
        Idea(3, ["tech", "hardware"]),
    ]
    generator = IdeaGenerator(ideas)
    tags = ["tech", "fashion", "design"]
    filtered_ideas = generator.filter_by_tags(tags)
    assert len(filtered_ideas) == 3
    assert filtered_ideas[0].id == 1
    assert filtered_ideas[1].id == 2
    assert filtered_ideas[2].id == 3

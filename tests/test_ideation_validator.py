import json
from ideation_validator import IdeationValidator, Idea

def test_generate_ideas():
    ideation_validator = IdeationValidator()
    ideas = ideation_validator.generate_ideas("remote work")
    
    assert len(ideas) >= 5
    titles = {idea.title for idea in ideas}
    assert len(titles) == len(ideas)
    for idea in ideas:
        assert isinstance(idea, Idea)
        assert "remote" in idea.title.lower() or "work" in idea.title.lower() or "remote" in idea.description.lower() or "work" in idea.description.lower()

def test_store_ideas():
    ideation_validator = IdeationValidator()
    ideas = [
        Idea("Remote Work Tracker", "A tool to track remote work hours."),
        Idea("Fitness Planner", "An app to plan daily fitness routines.")
    ]
    ideation_validator.store_ideas(ideas)
    
    assert len(ideation_validator.session) == 2
    stored_titles = {idea["title"] for idea in ideation_validator.session}
    expected_titles = {"Remote Work Tracker", "Fitness Planner"}
    assert stored_titles == expected_titles

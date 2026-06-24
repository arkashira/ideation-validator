import pytest
from ideation_validator import IdeationValidator, Idea

def test_add_idea():
    validator = IdeationValidator()
    idea = Idea('Test Idea', 1000.0, 0.8)
    validator.add_idea(idea)
    assert len(validator.ideas) == 1

def test_prioritize_roadmap_revenue_potential():
    validator = IdeationValidator()
    idea1 = Idea('Idea 1', 1000.0, 0.8)
    idea2 = Idea('Idea 2', 500.0, 0.9)
    validator.add_idea(idea1)
    validator.add_idea(idea2)
    roadmap = validator.prioritize_roadmap('revenue_potential')
    assert roadmap[0].name == 'Idea 1'

def test_prioritize_roadmap_validation_score():
    validator = IdeationValidator()
    idea1 = Idea('Idea 1', 1000.0, 0.8)
    idea2 = Idea('Idea 2', 500.0, 0.9)
    validator.add_idea(idea1)
    validator.add_idea(idea2)
    roadmap = validator.prioritize_roadmap('validation_score')
    assert roadmap[0].name == 'Idea 2'

def test_estimate_revenue():
    validator = IdeationValidator()
    idea = Idea('Test Idea', 1000.0, 0.8)
    assert validator.estimate_revenue(idea) == 1000.0

def test_validate_idea():
    validator = IdeationValidator()
    idea = Idea('Test Idea', 1000.0, 0.8)
    assert validator.validate_idea(idea) == 0.8

def test_invalid_sort_by():
    validator = IdeationValidator()
    with pytest.raises(ValueError):
        validator.prioritize_roadmap('invalid_sort_by')

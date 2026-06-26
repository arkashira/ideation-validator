from ideation_validator import IdeationValidator, Idea
import pytest
import time

def test_calculate_score():
    validator = IdeationValidator()
    idea = Idea("Test Idea", "This is a test idea")
    score = validator.calculate_score(idea)
    assert score == len("Test Idea") + len("This is a test idea")

def test_generate_explanation():
    validator = IdeationValidator()
    idea = Idea("Test Idea", "This is a test idea")
    score = 10
    explanation = validator.generate_explanation(idea, score)
    assert explanation.startswith("The idea 'Test Idea'")

def test_validate_idea():
    validator = IdeationValidator()
    idea = Idea("Test Idea", "This is a test idea")
    result = validator.validate_idea(idea)
    assert "score" in result
    assert "explanation" in result

def test_validate_idea_explanation_generation_time():
    validator = IdeationValidator()
    idea = Idea("Test Idea", "This is a test idea")
    with pytest.raises(ValueError):
        # Simulate slow explanation generation
        def slow_generate_explanation(self, idea, score):
            time.sleep(2)
            return f"The idea '{idea.name}' has a score of {score} because it has a descriptive name and description."
        original_method = validator.generate_explanation
        validator.generate_explanation = lambda idea, score: slow_generate_explanation(validator, idea, score)
        validator.validate_idea(idea)
        validator.generate_explanation = original_method

from ideation_validator import IdeationValidator, Idea

def test_generate_ideas():
    validator = IdeationValidator()
    text = "software development"
    ideas = validator.generate_ideas(text)
    assert len(ideas) == 2
    assert ideas[0].name == "software"
    assert ideas[1].name == "development"

def test_validate_idea():
    validator = IdeationValidator()
    idea = Idea("test", "A software tool for test", 0.4, 1000.0)
    assert validator.validate_idea(idea) == True
    idea = Idea("test", "A software tool for test", 0.2, 1000.0)
    assert validator.validate_idea(idea) == False

def test_get_validated_ideas():
    validator = IdeationValidator()
    text = "software development"
    validated_ideas = validator.get_validated_ideas(text)
    assert len(validated_ideas) == 2
    assert validated_ideas[0].name == "software"
    assert validated_ideas[1].name == "development"

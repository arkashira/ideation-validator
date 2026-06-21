from ideation_validator import IdeaValidator, IdeaRequest
import pytest
from datetime import datetime, timedelta

def test_log_idea():
    validator = IdeaValidator()
    validator.log_idea("test_keyword", ["tag1", "tag2"], 1)
    assert len(validator.get_ideas()) == 1
    idea = validator.get_ideas()[0]
    assert idea.keyword == "test_keyword"
    assert idea.tags == ["tag1", "tag2"]
    assert idea.user_id == 1

def test_filter_ideas_by_retention_policy():
    validator = IdeaValidator()
    validator.log_idea("test_keyword1", ["tag1", "tag2"], 1)
    idea = IdeaRequest(
        timestamp=(datetime.now() - timedelta(days=730)).isoformat(),
        keyword="test_keyword2",
        tags=["tag3", "tag4"],
        user_id=2
    )
    validator.ideas.append(idea)
    filtered_ideas = validator.filter_ideas_by_retention_policy(2)
    assert len(filtered_ideas) == 2

def test_filter_ideas_by_retention_policy_edge_case():
    validator = IdeaValidator()
    idea = IdeaRequest(
        timestamp=(datetime.now() - timedelta(days=730)).isoformat(),
        keyword="test_keyword2",
        tags=["tag3", "tag4"],
        user_id=2
    )
    validator.ideas.append(idea)
    filtered_ideas = validator.filter_ideas_by_retention_policy(1)
    assert len(filtered_ideas) == 0

import pytest
from src.ideation_validator import Idea, IdeationValidator, load_ideas

def test_get_validation_metrics() -> None:
    idea = Idea("Idea 1", 100, 50, 10, [1, 2, 3])
    validator = IdeationValidator([idea])
    metrics = validator.get_validation_metrics(idea)
    assert metrics["monthly_search_volume"] == "100"
    assert metrics["google_trends_score"] == "50"
    assert metrics["competing_products"] == "10"
    assert metrics["trend_graph"] == "[1, 2, 3]"

def test_refresh_data() -> None:
    idea = Idea("Idea 1", 100, 50, 10, [1, 2, 3])
    validator = IdeationValidator([idea])
    validator.refresh_data()
    assert idea.monthly_search_volume == 101
    assert idea.google_trends_score == 51
    assert idea.competing_products == 11
    assert idea.trend_graph == [1, 2, 3, 1]

def test_get_data_sources() -> None:
    idea = Idea("Idea 1", 100, 50, 10, [1, 2, 3])
    validator = IdeationValidator([idea])
    data_sources = validator.get_data_sources()
    assert data_sources["monthly_search_volume"] == "Google Keyword Planner"
    assert data_sources["google_trends_score"] == "Google Trends"
    assert data_sources["competing_products"] == "Product Hunt"
    assert data_sources["trend_graph"] == "Google Trends"

def test_get_idea_list() -> None:
    idea1 = Idea("Idea 1", 100, 50, 10, [1, 2, 3])
    idea2 = Idea("Idea 2", 200, 60, 20, [4, 5, 6])
    validator = IdeationValidator([idea1, idea2])
    idea_list = validator.get_idea_list()
    assert len(idea_list) == 2
    assert idea_list[0].name == "Idea 1"
    assert idea_list[1].name == "Idea 2"

def test_load_ideas() -> None:
    ideas = load_ideas()
    assert len(ideas) == 3
    assert ideas[0].name == "Idea 1"
    assert ideas[1].name == "Idea 2"
    assert ideas[2].name == "Idea 3"

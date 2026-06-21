from ideation_validator import IdeationValidator, Idea, load_ideas_from_json
import pytest
from datetime import datetime, timedelta

def test_get_validation_metrics():
    idea = Idea(
        name="Test Idea",
        monthly_search_volume=100,
        google_trends_score=50,
        competing_products=10,
        trend_graph=[1, 2, 3]
    )
    validator = IdeationValidator([idea])
    metrics = validator.get_validation_metrics(idea)
    assert metrics["monthly_search_volume"] == 100
    assert metrics["google_trends_score"] == 50
    assert metrics["competing_products"] == 10
    assert metrics["trend_graph"] == [1, 2, 3]

def test_refresh_data():
    idea = Idea(
        name="Test Idea",
        monthly_search_volume=100,
        google_trends_score=50,
        competing_products=10,
        trend_graph=[1, 2, 3]
    )
    validator = IdeationValidator([idea])
    validator.refresh_data()
    assert idea.monthly_search_volume == 101
    assert idea.google_trends_score == 51
    assert idea.competing_products == 11
    assert idea.trend_graph == [1, 2, 3, 1]

def test_get_data_sources():
    idea = Idea(
        name="Test Idea",
        monthly_search_volume=100,
        google_trends_score=50,
        competing_products=10,
        trend_graph=[1, 2, 3]
    )
    validator = IdeationValidator([idea])
    data_sources = validator.get_data_sources()
    assert data_sources["monthly_search_volume"] == "Google Trends"
    assert data_sources["google_trends_score"] == "Google Trends"
    assert data_sources["competing_products"] == "Product Hunt"
    assert data_sources["trend_graph"] == "Google Trends"

def test_load_ideas_from_json():
    json_data = """
    [
        {
            "name": "Test Idea 1",
            "monthly_search_volume": 100,
            "google_trends_score": 50,
            "competing_products": 10,
            "trend_graph": [1, 2, 3]
        },
        {
            "name": "Test Idea 2",
            "monthly_search_volume": 200,
            "google_trends_score": 60,
            "competing_products": 20,
            "trend_graph": [4, 5, 6]
        }
    ]
    """
    ideas = load_ideas_from_json(json_data)
    assert len(ideas) == 2
    assert ideas[0].name == "Test Idea 1"
    assert ideas[0].monthly_search_volume == 100
    assert ideas[0].google_trends_score == 50
    assert ideas[0].competing_products == 10
    assert ideas[0].trend_graph == [1, 2, 3]
    assert ideas[1].name == "Test Idea 2"
    assert ideas[1].monthly_search_volume == 200
    assert ideas[1].google_trends_score == 60
    assert ideas[1].competing_products == 20
    assert ideas[1].trend_graph == [4, 5, 6]

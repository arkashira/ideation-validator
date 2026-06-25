from ideation_validator import IdeationValidator, Idea, load_ideas

def test_get_validation_metrics():
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    metrics = validator.get_validation_metrics("Idea 1")
    assert metrics["monthly_search_volume"] == 100
    assert metrics["google_trends_score"] == 50
    assert metrics["competing_products"] == 10
    assert metrics["trend_graph"] == [1, 2, 3]

def test_get_validation_metrics_idea_not_found():
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    metrics = validator.get_validation_metrics("Idea 3")
    assert metrics["error"] == "Idea not found"

def test_refresh_data():
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    validator.refresh_data()
    assert ideas[0].monthly_search_volume == 101
    assert ideas[0].google_trends_score == 51
    assert ideas[0].competing_products == 11
    assert ideas[0].trend_graph == [1, 2, 3, 1]

def test_get_credits():
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    credits = validator.get_credits("Idea 1")
    assert credits["monthly_search_volume"] == "Google Trends"
    assert credits["google_trends_score"] == "Google Trends"
    assert credits["competing_products"] == "Product Hunt"
    assert credits["trend_graph"] == "Google Trends"

def test_get_credits_idea_not_found():
    ideas = load_ideas()
    validator = IdeationValidator(ideas)
    credits = validator.get_credits("Idea 3")
    assert credits["error"] == "Idea not found"

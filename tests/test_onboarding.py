from src.onboarding import IdeationValidator
import pytest

def test_start_tour():
    validator = IdeationValidator()
    result = validator.start_tour()
    assert result == "Tour completed"

def test_skip_tour():
    validator = IdeationValidator()
    result = validator.skip_tour()
    assert result == "Tour skipped"
    assert validator.get_settings()["tour_skipped"] == True

def test_replay_tour():
    validator = IdeationValidator()
    validator.skip_tour()
    result = validator.replay_tour()
    assert result == "Tour completed"
    assert validator.get_settings()["tour_replayed"] == True

def test_tour_completion_time():
    validator = IdeationValidator()
    import time
    start_time = time.time()
    validator.start_tour()
    end_time = time.time()
    assert end_time - start_time < 30

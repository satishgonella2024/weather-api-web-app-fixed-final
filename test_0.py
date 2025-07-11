import pytest

# Fixture example
@pytest.fixture
def example_fixture():
    return "example"

# Mock example
class MockWeatherAPI:
    def get_weather(self, location):
        return {"location": location, "temperature": 25}

def test_valid_input(example_fixture):
    assert example_fixture == "example"

def test_invalid_input():
    with pytest.raises(ValueError):
        raise ValueError

def test_boundary_conditions():
    assert 1 + 1 == 2

def test_error_handling():
    with pytest.raises(TypeError):
        raise TypeError

def test_weather_api_integration():
    mock_api = MockWeatherAPI()
    weather_data = mock_api.get_weather("New York")
    assert weather_data["location"] == "New York"
    assert weather_data["temperature"] == 25
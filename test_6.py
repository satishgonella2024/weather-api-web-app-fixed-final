import pytest

def add(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

    with pytest.raises(TypeError):
        add('1', 2)

class MockWeatherAPI:
    def get_weather(self, city):
        return {'temperature': 25, 'conditions': 'sunny'}

@pytest.fixture
def setup():
    # Setup code here
    yield
    # Teardown code here

def test_weather_display(setup):
    api = MockWeatherAPI()
    weather_data = api.get_weather('New York')
    assert weather_data['temperature'] == 25
    assert weather_data['conditions'] == 'sunny'
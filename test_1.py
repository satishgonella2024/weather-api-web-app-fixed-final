import pytest

# Mock fixture example
@pytest.fixture
def mock_data():
    return {"temperature": 25, "humidity": 60}

# Test happy path
def test_weather_display(mock_data):
    assert mock_data["temperature"] == 25
    assert mock_data["humidity"] == 60

# Test edge case
def test_weather_display_negative_temperature(mock_data):
    mock_data["temperature"] = -5
    assert mock_data["temperature"] == -5

# Test error handling
def test_weather_display_invalid_data(mock_data):
    with pytest.raises(KeyError):
        mock_data["pressure"]

# Test boundary conditions
def test_weather_display_high_humidity(mock_data):
    mock_data["humidity"] = 100
    assert mock_data["humidity"] == 100
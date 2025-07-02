"""Tests weather_service.py module using pytest and requests-mock."""

import requests
from weather_service import WeatherService
import dt_conversion

def test_get_weather_data_success(requests_mock, monkeypatch):
    """Test successful processing of weather data from the API."""

    # Create fake JSON response that the API would return
    fake_json = {
   "coord": {
      "lon": 0,
      "lat": 0
   },
   "weather": [
      {
         "main": "Rain",
         "description": "clear sky",
      }
   ],
   "main": {
      "temp": 22.5,
      "humidity": 55,
   },
   "dt": 1609459200,
   "name": "TestCity",
   "cod": 200
}

    # replace the real API call using requests_mock and returning the fake JSON
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        json=fake_json,
        status_code=200
    )

    ws = WeatherService(api_key="DUMMY_KEY") # Create instance of WeatherService with a fake API key
    result = ws.get_weather_data("TestCity") # Call the method to get weather data for "TestCity"

    # Assert that the result is a dictionary with expected keys and values
    assert result["city"] == "TestCity"
    assert result["temperature"] == 22.5
    assert result["humidity"] == 55
    assert result["condition"] == "clear sky"
    # Accept either UTC or GMT for local time as both are valid representations
    assert (
        result["local_time"] == "01-Jan-21 12:00 AM UTC" or
        result["local_time"] == "01-Jan-21 12:00 AM GMT"
    )


def test_get_weather_data_timeout(requests_mock, capsys):
    """Test handling of a timeout when retrieving weather data from the API."""

    # Simulate a timeout when requests.get is called using requests_mock
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        exc=requests.exceptions.Timeout
    )
    ws = WeatherService(api_key="DUMMY_KEY") # Create instance of WeatherService with fake API key
    result = ws.get_weather_data("TestCity") # Call the method to get weather data for "TestCity"
    captured = capsys.readouterr() # Capture printed output

    # Assert that the result is an empty dictionary and the correct error message is printed
    assert result == {}, "On timeout, should return empty dict"
    assert "Error: Request timed out (10 seconds)" in captured.out


def test_get_weather_data_connection_error(requests_mock, capsys):
    """Test handling of a connection error when retrieving weather data from the API."""

    # Simulate a connection error when requests.get is called using requests_mock
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        exc=requests.exceptions.ConnectionError
    )
    ws = WeatherService(api_key="DUMMY_KEY") # Create instance of WeatherService with fake API key
    result = ws.get_weather_data("TestCity") # Call the method to get weather data for "TestCity"
    captured = capsys.readouterr() # Capture printed output

    # Assert that the result is an empty dictionary and the correct error message is printed
    assert result == {}, "On timeout, should return empty dict"
    assert "Error: Unable to connect to the OpenWeatherMap API" in captured.out


def test_get_weather_data_http_error(requests_mock, capsys):
    """Test handling of HTTP error when retrieving weather data from the API."""

    # Simulate an HTTP error (eg. 404 Not Found) when requests.get is called using requests_mock
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        status_code=404,
        reason="Not Found"
    )
    ws = WeatherService(api_key="DUMMY_KEY") # Create instance of WeatherService with fake API key
    result = ws.get_weather_data("TestCity") # Call the method to get weather data for "TestCity"
    captured = capsys.readouterr() # Capture printed output

    # Assert that the result is an empty dictionary and the correct error message is printed
    assert result == {}
    assert "HTTP Error: 404 - Not Found" in captured.out


def test_get_weather_data_generic_exception(monkeypatch, capsys):
    """Test handling of an unexpected request exception when retrieving weather data."""

    # Patch requests.get to raise a raw RequestException (not HTTPError, Timeout, etc.)
    def raise_req_exception(*args, **kwargs):
        """Function to raise a RequestException for testing purposes."""

        raise requests.RequestException("test error") # Simulate a generic request exception

    # Replace requests.get with our function that raises an exception
    monkeypatch.setattr(requests, "get", raise_req_exception)

    ws = WeatherService(api_key="KEY") # Create instance of WeatherService with a fake API key
    result = ws.get_weather_data("City") # Call the method to get weather data for "City"
    captured = capsys.readouterr() # Capture printed output

    # Assert that the result is an empty dictionary and the correct error message is printed
    assert result == {}
    assert "Network Error: test error" in captured.out


def test_get_weather_data_key_error(requests_mock, capsys, monkeypatch):
    """Test handling of KeyError when retrieving weather data from the API."""

    # Return JSON with missing expected fields
    broken_json = {
        "name": "City",
        "main": {},  # missing 'temp'
        "weather": [],  # missing [0]['description']
        "dt": 123456789,
        "coord": {"lat": 0, "lon": 0}
    }

    # Fake the API response to return the broken JSON
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        json=broken_json,
        status_code=200
    )

    ws = WeatherService(api_key="KEY") # Create instance of WeatherService with a fake API key
    result = ws.get_weather_data("City") # Call the method to get weather data for "City"
    captured = capsys.readouterr() # Capture printed output

    # Assert that the result is an empty dictionary and the correct error message is printed
    assert result == {} 
    assert "Data Error: Missing expected field" in captured.out

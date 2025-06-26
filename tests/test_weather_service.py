"""Tests weather_service.py module using pytest and requests-mock."""

import requests
from weather_service import WeatherService
import dt_conversion

def test_get_weather_data_success(requests_mock, monkeypatch):
    """Test successful retrieval of weather data from the API."""

    #Prepare a fake JSON payload
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
    # Stub out dt_conversion.convert_time so we don't test datetime
    monkeypatch.setattr(dt_conversion, "convert_time",
                        lambda unix_dt, coords: "01-Jan-21 12:00 AM UTC")
    # Intercept the GET request, regardless of params, return our fake JSON
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        json=fake_json,
        status_code=200
    )

    # --- Act ---
    ws = WeatherService(api_key="DUMMY_KEY")
    result = ws.get_weather_data("TestCity")

    # --- Assert ---
    assert result["city"] == "TestCity"
    assert result["temperature"] == 22.5
    assert result["humidity"] == 55
    assert result["condition"] == "clear sky"
    assert (
        result["local_time"] == "01-Jan-21 12:00 AM UTC" or
        result["local_time"] == "01-Jan-21 12:00 AM GMT"
    )


def test_get_weather_data_timeout(requests_mock, capsys):
    """Test handling of a timeout when retrieving weather data from the API."""

    # Simulate a timeout when requests.get is called
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        exc=requests.exceptions.Timeout
    )

    ws = WeatherService(api_key="DUMMY_KEY")
    result = ws.get_weather_data("TestCity")

    # Capture printed output
    captured = capsys.readouterr()

    # --- Assert ---
    assert result == {}, "On timeout, should return empty dict"
    assert "Error: Request timed out (10 seconds)" in captured.out

def test_get_weather_data_connection_error(requests_mock, capsys):
    """Test handling of a timeout when retrieving weather data from the API."""

    # Simulate a timeout when requests.get is called
    requests_mock.get(
        "https://api.openweathermap.org/data/2.5/weather",
        exc=requests.exceptions.ConnectionError
    )

    ws = WeatherService(api_key="DUMMY_KEY")
    result = ws.get_weather_data("TestCity")

    # Capture printed output
    captured = capsys.readouterr()

    # --- Assert ---
    assert result == {}, "On timeout, should return empty dict"
    assert "Error: Unable to connect to the OpenWeatherMap API" in captured.out

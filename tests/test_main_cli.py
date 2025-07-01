"""Test the main() function in main.py, which is the CLI entry point."""

import builtins
import pytest
import main
from weather_service import WeatherService

class DummyHandler:
    """A simple dummy output handler to simulate terminal output."""

    def output(self, data):
        """Simulate outputting data to the terminal."""
        print(f"OUTPUT: {data}")


class InputDriver:
    """A class to simulate user input for testing purposes."""

    def __init__(self, responses):
        self._iter = iter(responses)

    def __call__(self, prompt=""):
        return next(self._iter)

def test_cli_happy_path(monkeypatch, capsys):
    """Test the main() function in main.py with a happy path scenario."""

    monkeypatch.setenv("OWM_API_KEY", "DUMMY")

    # Stub out the network call so we always get a valid dict
    monkeypatch.setattr(
        WeatherService, "get_weather_data",
        lambda self, city: {
            "city": city,
            "temperature": 20,
            "humidity": 50,
            "condition": "sunny",
            "local_time": "01-Jan-21 12:00 AM UTC"
        }
    )

    # Patch the class imported in main.py
    monkeypatch.setattr(main, "TerminalOutput", DummyHandler)

    # Simulate typing: [menu choice, city name, exit]
    responses = ["1", "TestCity", "exit"]
    monkeypatch.setattr(builtins, "input", InputDriver(responses))

    # Run main(); it'll call exit() on "exit", so catch the SystemExit
    with pytest.raises(SystemExit):
        main.main()

    # Grab what was printed and verify our DummyHandler ran
    out = capsys.readouterr().out
    assert "OUTPUT: {'city': 'testcity', 'temperature': 20, 'humidity': 50" in out

def test_cli_no_data_error(monkeypatch, capsys):
    """Test the main() function in main.py when no data is returned for a city."""

    # Provide the API key so main() doesn’t exit early
    monkeypatch.setenv("OWM_API_KEY", "DUMMY")

    # Stub WeatherService.get_weather_data() to return {} (no data)
    monkeypatch.setattr(
        WeatherService, "get_weather_data",
        lambda self, city: {}
    )

    # Patch main.TerminalOutput so get_output_handler() uses DummyHandler
    monkeypatch.setattr(main, "TerminalOutput", DummyHandler)

    # Simulate user input: choose Terminal (1), enter BadCity, then exit
    driver = InputDriver(["1", "BadCity", "exit"])
    monkeypatch.setattr(builtins, "input", driver)

    # Run main.main() and catch the SystemExit from exit()
    with pytest.raises(SystemExit):
        main.main()

    # Capture printed output and assert the ValueError message shows
    out = capsys.readouterr().out
    assert "Value Error: No data found for the specified city." in out

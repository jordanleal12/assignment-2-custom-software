"""Smoke tests for main CLI application, the entry point for the application."""

import builtins # Used to mock user input
import pytest # Used for testing
import main # Main application module
from weather_service import WeatherService # Weather service module

class FakeOutputHandler:
    """Simulates terminal output for testing"""

    def output(self, data):
        """Provides a fake output for pytest instead of printing to terminal"""

        print(f"OUTPUT: {data}") # This will be captured by pytest

class FakeInputWriter:
    """Simulates user input sequence for testing"""

    def __init__(self, inputs):
        """Constructs an instance with a list of inputs to be iterated over"""

        # Convert list to iterator, giving us next item from list each time it's called
        self.inputs = iter(inputs)

    def __call__(self, prompt=""):
        """Returns next input in sequence by making the object callable like a function"""

        # Use next() to get the next input from the iterator above
        return next(self.inputs)

def setup_test_env(monkeypatch, weather_data_func, inputs):
    """Sets up the test environment by faking api key, weather service response, and user input"""

    # Sets the environment variable with fake API key for pytest
    monkeypatch.setenv("OWM_API_KEY", "TEST_KEY")

    # Replace weather service response with a mock function that returns predefined data
    monkeypatch.setattr(WeatherService, "get_weather_data", weather_data_func)

    # Use replace real output handler with a fake one for testing
    monkeypatch.setattr(main, "TerminalOutput", FakeOutputHandler)

    # Simulate user inputs by replacing built-in input function with our fake input writer
    monkeypatch.setattr(builtins, "input", FakeInputWriter(inputs))

def test_successful_weather_fetch(monkeypatch, capsys):
    """Tests weather data is fetched correctly with valid city input, captures output with capsys"""

    # Setup mock weather data
    def fake_weather_data(self, city):
        """Returns fake weather data for testing purposes without making actual API calls"""

        return {
            "city": city,
            "temperature": 20,
            "humidity": 50,
            "condition": "sunny",
            "local_time": "01-Jan-21 12:00 AM UTC"
        }

    # Configure test environment with fake weather data and user inputs
    setup_test_env(monkeypatch, fake_weather_data, ["1", "TestCity", "exit"])

    # Execute main function using with pytest.raises to verify SystemExit is raised on "exit"
    with pytest.raises(SystemExit):
        main.main()
    output = capsys.readouterr().out # Capture the output printed to terminal

    # Assert output matches expected values
    assert "OUTPUT: {'city': 'testcity'" in output
    assert "'temperature': 20" in output
    assert "'humidity': 50" in output
    assert "'condition': 'sunny'" in output
    assert "'local_time': '01-Jan-21 12:00 AM UTC'" in output

def test_invalid_city_handling(monkeypatch, capsys):
    """Tests error handling for non-existent city"""

    # Setup fake API call to return empty data
    def fake_weather_data(self, city):
        return {}

    # Configure test environment with fake weather data and user inputs
    setup_test_env(
        monkeypatch,
        fake_weather_data,
        ["1", "InvalidCity", "exit"]
    )

    # Execute main function using with pytest.raises to verify SystemExit is raised on "exit"
    with pytest.raises(SystemExit):
        main.main()
    output = capsys.readouterr().out

    # Assert output contains expected error message for no data found
    assert "Value Error: No data found for the specified city." in output

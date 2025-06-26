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


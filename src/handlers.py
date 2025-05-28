""" This module defines classes for outputting weather data to terminal, CSV, and JSON."""

import json
from abc import ABC, abstractmethod
# import os
import csv

class DataOutput(ABC):
    """Abstract base class for weather data output."""

    def __init__(self, filename=None):
        """Initialize the filename for CSV and JSON if provided, ignores for terminal."""
        self.filename = filename

    @abstractmethod
    def output(self, weather_data: dict):
        """Abstract method to output weather data."""


class TerminalOutput(DataOutput):
    """Outputs weather data to the terminal."""

    def output(self, weather_data: dict) -> str:
        """Print the weather data to the terminal."""

        print(f"""Weather Data:
            Location: {weather_data["city"]}
            Temperature: {weather_data["temperature"]}°C
            Humidity: {weather_data["humidity"]}%
            Condition: {weather_data["condition"]}
            Current Time: {weather_data["current_time"]}
            {"-" * 20}""")

class CSVOutput(DataOutput):
    """Outputs the weather data to a CSV file."""

    def __init__(self, filename="weather_data.csv"):
        """Creates the filename for CSV output."""
        super().__init__(filename)

    def output(self, weather_data: dict) -> csv:
        """Save one weather report at a time"""

        # Creating and writing to the CSV file
        with open(self.filename, "w", newline="", encoding="utf-8") as f:
            # Create CSV writer with weather data keys as headers
            w = csv.DictWriter(f, fieldnames=weather_data.keys())
            w.writeheader() # Write the header row with the keys
            w.writerow(weather_data) # Write the weather data as a row in the CSV file

class JSONOutput(DataOutput):
    """Outputs the weather data to a JSON file."""

    def __init__(self, filename="weather_data.json"):
        """Creates the filename for JSON output."""
        super().__init__(filename)

    def output(self, weather_data: dict) -> json:
        # Converts the weather data dictionary to JSON format and writes it to a file.
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(weather_data, f, indent=4)

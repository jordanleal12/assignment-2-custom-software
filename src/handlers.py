""" This module defines classes for outputting weather data to terminal, CSV, and JSON."""

import json # Used to handle JSON data
from abc import ABC, abstractmethod # Creates abstract base classes for structure and method definitions
import csv # Used to handle CSV data

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

        print(f"""
            Weather Data:
            Location: {weather_data["city"]}
            Temperature: {weather_data["temperature"]}°C
            Humidity: {weather_data["humidity"]}%
            Condition: {weather_data["condition"]}
            Local Time: {weather_data["local_time"]}
            {"-" * 20}""")

class CSVOutput(DataOutput):
    """Outputs the weather data to a CSV file."""

    def __init__(self, filename="weather_data.csv"):
        """Creates the filename for CSV output."""
        super().__init__(filename)

    def output(self, weather_data: dict) -> csv:
        """Creates and writes the CSV file with error checking."""

        try: # Try to open the file for writing
            with open(self.filename, "w", newline="", encoding="utf-8") as f:
                # Create CSV writer with weather data keys as headers
                w = csv.DictWriter(f, fieldnames=weather_data.keys())
                w.writeheader() # Write the header row with the keys
                w.writerow(weather_data) # Write the weather data as a row in the CSV file
                print(f"Weather data written to {self.filename}") # Print success message
        except IOError as e: # Handle file writing errors such as permission or disk space issues
            print(f"Error writing to CSV file: {e}")

class JSONOutput(DataOutput):
    """Outputs the weather data to a JSON file."""

    def __init__(self, filename="weather_data.json"):
        """Creates the filename for JSON output."""
        super().__init__(filename)

    def output(self, weather_data: dict) -> json:
        """Creates and writes the JSON file with error checking."""

        try: # Try to open the file for writing
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(weather_data, f, indent=4) # Write to JSON with indentation
                print(f"Weather data written to {self.filename}") # Print success message
        except IOError as e:  # Handle file writing errors such as permission or disk space issues
            print(f"Error writing to JSON file: {e}")

from abc import ABC, abstractmethod # Used to make abstract classes

class DataOutput(ABC):
    '''Abstract base class for weather data output.'''

    def __init__(self, filename=None):
        '''Initialize the filename for CSV and JSON if provided, ignores for terminal.'''
        self.filename = filename

    @abstractmethod
    def output(self, weather_data: dict):
        '''Abstract method to output weather data.'''


class TerminalOutput(DataOutput):
    '''Outputs weather data to the terminal.'''

    def output(self, weather_data: dict):
        '''Print the weather data to the terminal.'''
        local_time = weather_data["current_time"] # Will use pytz to format time later
        print(f"""Weather Data:
            Location: {weather_data["city"]}
            Temperature: {weather_data["temperature"]}°C
            Humidity: {weather_data["humidity"]}%
            Condition: {weather_data["condition"]}
            Current Time: {local_time}
            {"-" * 20}""")


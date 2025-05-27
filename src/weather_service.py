import requests # Used to make HTTP requests
from dt_conversion import convert_time  # Importing the convert_time function from dt_conversion module

class WeatherService:
    '''Class to pull weather data from a weather API.'''

    def __init__(self, api_key: str):
        '''Create instance with API key and OpenWeatherMap URL.'''
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather" # OpenWeatherMap API URL

    def get_weather_data(self, city=str) -> dict:
        '''Fetch weather data from the API for the specified city.'''
        
        # Provides the parameters for OpenWeatherMap API request
        owm_queries = {
            "q": city,  # City name
            "appid": self.api_key,  # API key
            "units": "metric",  # Use metric units for temperature
            "lang": "en"  # Set language to English
        }

        # Use try/except to make API request in case of errors
        response = None  # Initialize response to None
        try:
            # Send web request to OpenWeatherMap API with above parameters
            response = requests.get(self.url, params=owm_queries, timeout=10) 
            # Returns a HTTP error if the request was unsuccessful, returns nothing otherwise
            response.raise_for_status()

        # Prints relevant error message if the request was unsuccessful
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
        
        if response is not None:  # Check if response is not None before accessing it
            data = response.json() # Assign response data to a variable
            # Return dictionary from json variable 
            return {
                "city": data["name"],  # City name
                "temperature": data["main"]["temp"],  # Temperature in Celsius
                "humidity": data["main"]["humidity"],  # Humidity percentage
                "condition": data["weather"][0]["description"],  # Weather description
                "current_time": convert_time(data["dt"], data["coord"])  # Current time in the city's timezone
            }
        return {}  # Return an empty dictionary if response is None

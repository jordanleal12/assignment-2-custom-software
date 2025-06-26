"""Define a class to pull weather data from API, convert to dictionary, and handle errors."""

import requests # Used to make HTTP requests
from dt_conversion import convert_time  # Import convert_time function from dt_conversion module

class WeatherService:
    """Class to pull weather data from a weather API."""

    def __init__(self, api_key: str):
        """Create instance with API key and OpenWeatherMap URL."""
        self.api_key = api_key # Store the API key for authentication
        self.url = "https://api.openweathermap.org/data/2.5/weather" # OpenWeatherMap API URL

    def get_weather_data(self, city=str) -> dict:
        """Fetch weather data from the API for the specified city."""

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
        # Prints relevant error message and returns empty dictionary if the request was unsuccessful
            data = response.json() # Assign response data to a variable
            # Return dictionary from json variable
            return {
                "city": data["name"],  # City name
                "temperature": data["main"]["temp"],  # Temperature in Celsius
                "humidity": data["main"]["humidity"],  # Humidity percentage
                "condition": data["weather"][0]["description"],  # Weather description
                "local_time": convert_time(data["dt"], data["coord"])  # Local time of last update
            }
        except requests.ConnectionError:
            print("Error: Unable to connect to the OpenWeatherMap API")
            return {}
        except requests.Timeout:
            print("Error: Request timed out (10 seconds)")
            return {}
        except requests.HTTPError as e:
            print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
            return {}
        except requests.RequestException as e: # Catch all other request-related errors
            print(f"Network Error: {e}")
            return {}
        except KeyError as e:
            print(f"Data Error: Missing expected field {e}")
            return {}

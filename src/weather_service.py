import requests # Used to make HTTP requests

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
        try:
            # Send web request to OpenWeatherMap API with above parameters
            response = requests.get(self.base_url, params=owm_queries) 
            # Returns a HTTP error if the request was unsuccessful, returns nothing otherwise
            response.raise_for_status()
            # Uses requests to convert the received weather data to JSON format
            data = response.json() 
            return {
                "city": data["name"],  # City name
                "temperature": data["main"]["temp"],  # Temperature in Celsius
                "humidity": data["main"]["humidity"],  # Humidity percentage
                "condition": data["weather"][0]["description"],  # Weather description
                "current_time": convert_time(data["dt"], data["timezone"], data["coord"])  # Current time in the city's timezone
            }
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return {}
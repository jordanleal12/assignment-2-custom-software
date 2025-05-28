""" Takes input from the user, fetches weather data, and outputs it in the selected format. """

import os
from dotenv import load_dotenv
from handlers import TerminalOutput, CSVOutput, JSONOutput
from weather_service import WeatherService

# Add output selection
def get_output_handler():
    """Prompts user to select output format and returns the corresponding handler."""
    
    while True:
        choice = input("""
                   Choose output format:
                   1. Terminal
                   2. CSV File
                   3. JSON File
                   Enter choice (1-3): 
                   """).strip()
        match choice: # Matches user input to select output and returns error if invalid
            case '1':
                return TerminalOutput()
            case '2':
                filename = input(
                    "Enter CSV filename (default: weather_data.csv): "
                    ) or 'weather_data.csv'
                return CSVOutput(filename)
            case '3':
                filename = input(
                    "Enter JSON filename (default: weather_data.json): "
                    ) or 'weather_data.json'
                return JSONOutput(filename)
            case _:
                print("\nInvalid choice, please enter 1, 2, or 3.")

# Modify main loop
def main():
    """ Main function to run the weather application. """
    load_dotenv()
    api_key = os.getenv("OWM_API_KEY")

    if not api_key:
        print("Error: Missing API key in .env file")
        return

    service = WeatherService(api_key)
    handler = get_output_handler()  # Updated

    while True:
        city = input("\nEnter city name (or 'exit'): ")
        if city.lower() == "exit":
            break

        try:
            weather_data = service.get_weather_data(city)
            if weather_data:
                handler.output(weather_data)
                print("Data saved successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")

main()

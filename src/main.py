""" Takes input from the user, fetches weather data, and outputs it in the selected format. """

import os
from dotenv import load_dotenv
from handlers import TerminalOutput, CSVOutput, JSONOutput
from weather_service import WeatherService

def extension_checker(filename: str, f_type: str) -> str:
    """Checks the file extension and returns the filename with the correct extension."""
    ext = os.path.splitext(filename)[1].lower()
    if ext and ext != f_type:
        print(f"Invalid file extension, converting to {f_type}")
        filename = filename.replace(ext, f_type)
    if not ext:
        print(f"Missing file extension, adding {f_type}")
        filename += f_type
    return filename

# Add output selection
def get_output_handler():
    """Prompts user to select output format and returns the corresponding handler."""

    print(f"""
    Welcome to the Weather Application!
    This app fetches current weather, date and time from any Capital City in the world!
    You can choose to output to terminal, a CSV file, or a JSON file.
    Please note - You can choose non-capital cities, but the data may not be accurate.
    {'_' * 50}""")

    while True:
        choice = input("""
                Choose output format:
                1. Terminal
                2. CSV File
                3. JSON File
                4. Exit
                Enter choice (1-3): 
                   """).strip()
        match choice: # Matches user input to select output and returns error if invalid
            case '1':
                return TerminalOutput()
            case '2':
                filename = input(
                    "Enter CSV filename (default: weather_data.csv): "
                    ) or "weather_data.csv"
                filename = extension_checker(filename, ".csv") # Check and correct file extension
                return CSVOutput(filename)
            case '3':
                filename = input(
                    "Enter JSON filename (default: weather_data.json): "
                    ) or 'weather_data.json'
                filename = extension_checker(filename, ".json") # Check and correct file extension
                return JSONOutput(filename)
            case '4':
                print("Exiting the application. Goodbye!")
                exit()  # Exit the application
            case _:
                print("\nInvalid choice, please enter 1, 2, 3 or 4.")

# Modify main loop
def main():
    """ Main function to run the weather application. """
    load_dotenv()
    api_key = os.getenv("OWM_API_KEY")

    if not api_key:
        print("Error: Missing API key in .env file")
        exit()

    service = WeatherService(api_key)
    handler = get_output_handler()

    while True:
        city = input("\nEnter city name, 'exit' or 'return' to re-select output: ").lower().strip()
        match city:
            case "exit":
                exit()
            case "return":
                handler = get_output_handler()
            case "":
                print("City name cannot be empty. Please try again.")
            case _:
                try:
                    # Check if the city name contains only alphabetic characters
                    if not city.isalpha():
                        raise ValueError("City name must be letters only")
                    weather_data = service.get_weather_data(city)
                    # Check if weather data is not empty
                    if weather_data:
                        handler.output(weather_data)
                    else:
                        raise ValueError("No data found for the specified city.")
                except Exception as e:
                    print(f"Error: {e}")

if __name__ == "__main__":
    main() # Checks if the script is being run from main before calling

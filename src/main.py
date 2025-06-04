""" Takes input from the user, fetches weather data, and outputs it in the selected format. """

import os # Access environment variables and handle file paths
from dotenv import load_dotenv # Load environment variables from a .env file
from handlers import TerminalOutput, CSVOutput, JSONOutput # Import output handlers for different formats
from weather_service import WeatherService # Import WeatherService class to fetch weather data

def extension_checker(filename: str, f_type: str) -> str:
    """Checks the file extension and returns the filename with the correct extension."""

    ext = os.path.splitext(filename)[1].lower() # Get the file extension from the filename
    if ext and ext != f_type:
        print(f"Invalid file extension, converting to {f_type}")
        filename = filename.replace(ext, f_type) #replace the existing extension with the correct one
    if not ext:
        print(f"Missing file extension, adding {f_type}")
        filename += f_type # Add the correct file extension if missing
    return filename

def get_output_handler():
    """Prompts user to select output format and returns the corresponding handler."""

    print(f"""  
    Welcome to the Weather Application!
    This app fetches current weather, date and time from any Capital City in the world!
    You can choose to output to terminal, a CSV file, or a JSON file.
    The local time is from the last weather update, given every ~10 minutes.
    Multi-word city names can be separated by commas or spaces or use the first word only.
    If the city shares its name, add the ISO 3166 state and country code, (e.g. "melbourne nsw au"). 
    {"_" * 50}""")

    while True:
        choice = input("""
                Choose output format:
                1. Terminal
                2. CSV File
                3. JSON File
                4. Exit
                Enter choice (1-4): 
                """).strip()
        match choice: # Matches user input to select output and returns error if invalid
            case "1":
                return TerminalOutput()
            case "2":
                filename = input(
                    "Enter CSV filename (default: weather_data.csv): "
                    ) or "weather_data.csv" # Takes user input for filename or uses default
                filename = extension_checker(filename, ".csv") # Check and correct file extension
                return CSVOutput(filename)
            case "3":
                filename = input(
                    "Enter JSON filename (default: weather_data.json): "
                    ) or "weather_data.json" # Takes user input for filename or uses default
                filename = extension_checker(filename, ".json") # Check and correct file extension
                return JSONOutput(filename)
            case "4":
                print("Exiting the application. Goodbye!")
                exit()  # Exit the application
            case _:
                print("\nInvalid choice, please enter 1, 2, 3 or 4.")

def main():
    """ Main function to run the weather application. """

    load_dotenv() # Load environment variables from .env file
    api_key = os.getenv("OWM_API_KEY") # Get the API key from environment variables

    if not api_key: # Exit if API key is not found
        print("Error: Missing API key in .env file")
        exit()

    service = WeatherService(api_key) # Create an instance of WeatherService with the API key
    handler = get_output_handler() # Get the output handler based on user choice

    while True: # Loop to continuously prompt for city input until correct input is provided
        city = input("""
        Enter city name for weather report, 
        "exit" to close the application, or 
        "return" to change output/file name: 
        """).lower().strip()
        match city:
            case "exit": # Exit the application if user inputs "exit"
                exit()
            case "return": # Return to the output handler selection if user inputs "return"
                handler = get_output_handler()
            case "": # If the city name is empty, prompt the user to enter a valid city name
                print("City name cannot be empty. Please try again.")
            case _:
                try:
                    for char in city: # Check if the city name contains only alphabetic characters
                        if not char.isalpha() and char not in (" ", ","):
                            raise ValueError(
                                "City name must contain letters, spaces or commas only"
                                )
                    city = city.replace(" ", ",")  # Swap spaces with commas for multi-word cities
                    weather_data = service.get_weather_data(city)
                    if weather_data: # Check if weather data is not empty
                        handler.output(weather_data)
                    else: # If no data is returned, raise an error
                        raise ValueError("No data found for the specified city.")
                except ValueError as e:
                    print(f"Value Error: {e}")
                    
if __name__ == "__main__":
    main() # Checks if the script is being run from main before calling

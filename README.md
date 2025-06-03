# CLI Weather Application - Fetch Current Weather

## Overview

This is a python command line application that gives you current weather data for any capital city in the world!

The application will output current temperature, humidity, weather conditions and local time of the last update.

Non-capital cities also work, but functionality is only guaranteed for capital cities.

Users can choose to output the weather report to the terminal, CSV or JSON!

## Features

- Real time (within 10 minutes) weather data from any capital city
- Multiple output formats (terminal, JSON, CSV)
- Automatic conversion to local timezone, adding the abbreviation
- Simple and easy to use interface with robust error checking
- Easy to set up and install process

## Requirements

- Python 3.10+ (3.12.3 recommended)
- PIP (python package installer)
- OpenWeatherMap API Key (free, instructions provided in install section)

## Installation

- [Linux/WSL/Mac](#linuxwslmac)
- [Windows](#windows)

### Linux/WSL/Mac

1. Verify version

   ```bash
   python3 --version # Should show 3.10 or higher
   ```

2. Download and extract API to desired folder
   **OR**
   clone from [github repository](https://github.com/jordanleal12/assignment-2-custom-software)

   ```bash
   git clone https://github.com/jordanleal12/assignment-2-custom-software
   cd assignment-2-custom-software
   ```

3. Create the Virtual Environment

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Add OpenWeatherMap API key

   - Visit [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) sign up page and create account
   - Copy API key from [API keys](https://home.openweathermap.org/api_keys) page on OpenWeatherMap
   - Create a file named .env in the project root and save your API key

   ```bash
   echo "OWM_API_KEY = \"api-key-here\"" > .env
   # Replace api-key-here with the API key
   # MAKE SURE TO INCLUDE ESCAPED QUOTATION MARKS FOR API KEY!!!
   ```

6. Run application!

   ```bash
   python3 src/main.py
   ```

7. Deactivate when finished

   ```bash
   deactivate
   ```

### Windows

1. Verify version

   ```cmd
   python --version # Should show 3.10 or higher
   ```

2. Download and extract API to desired folder
   **OR**
   clone from [github repository](https://github.com/jordanleal12/assignment-2-custom-software)

   ```cmd
   git clone https://github.com/jordanleal12/assignment-2-custom-software
   cd assignment-2-custom-software
   ```

3. Create the Virtual Environment

   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. Install dependencies

   ```cmd
   pip install -r requirements.txt
   ```

5. Add OpenWeatherMap API key

   - Visit [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) sign up page and create account
   - Copy API key from [API keys](https://home.openweathermap.org/api_keys) page on OpenWeatherMap
   - Create a file named .env in the project root and save your API key

   ```cmd
   echo OWM_API_KEY = "api-key-here" > .env
   REM - Replace api-key-here with the API key
   REM - ENSURE API KEY IS IN QUOTATION MARKS
   ```

6. Run application!

   ```cmd
   python src\main.py
   ```

7. Deactivate when finished

   ```cmd
   deactivate
   ```

## Using the Weather App

1. From the main menu, type:
   - '1' To output the weather report to the CLI
   - '2' To output to a CSV file
   - '3' For a JSON file
   - '4' To exit the application
2. If selecting a CSV or JSON file, press enter to use the default file name, or input your own filename.

   Note: The new file will overwrite an existing file of the same name, so input a new filename for each unique file you wish to keep.

3. Enter:
   - City name to receive the current weather
   - 'Return' to re-select output or specify new file name to write to
   - 'Exit' to exit the application

## Additional Information

- City names with multiple names (i.e. Buenos Aires) can be input as comma separated, space separated or using the first word only
- The datetime received is the local time in the selected city from the last weather update.

  Since the updates occur approximately every 5 - 10 minutes, this shouldn't be used as an accurate representation of current time but rather an accurate representation of the time of the last weather update in that location

- City names and other inputs are insensitive to surrounding case and whitespace.
- If file names are entered incorrectly, they will automatically be fixed.

  If the incorrect extension is used, it will be replaced with the correct extension. If extension name is missing, it will be added.

## External Libraries

- Requests - Used for fetching data from the API
- Python-dotenv - Used for managing the API key
- Pytz - Used to convert timezones to local timezone
- Timezonefinder - Converts city coordinates to timezone suffix

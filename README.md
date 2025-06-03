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
- Windows, Linux or MacOS
- Active internet connection

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
   - Verify email address used with confirmation email - API KEY WILL NOT WORK IF YOU SKIP THIS STEP!!!
   - For ease of use, the following pre-confirmed API key can be used - "0c3330fa568c970e539a75c0d5c08c40"

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
   - Verify email address used with confirmation email - API KEY WILL NOT WORK IF YOU SKIP THIS STEP!!!
   - For ease of use, the following pre-confirmed API key can be used - "0c3330fa568c970e539a75c0d5c08c40"

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

## Files

|     **Files**      |                                   **Purpose**                                   |
| :----------------: | :-----------------------------------------------------------------------------: |
|        .env        |      Stores API key as environmental variable for accessing OpenWeatherMap      |
|      main.py       |             Entry point for application, executes main app function             |
|    handlers.py     |             Contains logic for outputting to terminal, CSV or JSON              |
| weather_service.py |     Communicates with OpenWeatherMap API to retrieve requested weather data     |
|  dt_conversion.py  | Contains logic for converting the weather data datetime to local aware datetime |

## External Libraries/Packages

| **Package/Library** | **Version** |                         **License**                         |                     **Purpose**                     |
| :-----------------: | :---------: | :---------------------------------------------------------: | :-------------------------------------------------: |
|       certifi       |  2025.4.26  |      [MPL 2.0](https://www.mozilla.org/en-US/MPL/2.0/)      |            SSL certificate verification             |
|        cffi         |   1.17.1    |          [MIT](https://opensource.org/license/MIT)          |          Foreign function interface for C           |
| charset-normalizer  |    3.4.2    |          [MIT](https://opensource.org/license/MIT)          |             Detects character encoding              |
|         h3          |    4.2.2    |  [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)  | Required by timezonefinder for geo-spatial indexing |
|        idna         |    3.10     | [BSD-3-Clause](https://opensource.org/license/BSD-3-Clause) |         Supports international domain names         |
|        numpy        |    2.2.6    | [BSD-3-Clause](https://opensource.org/license/BSD-3-Clause) | Required by timezonefinder for numerical operations |
|      pycparser      |    2.22     | [BSD-3-Clause](https://opensource.org/license/BSD-3-Clause) |                    Parses C code                    |
|    python-dotenv    |    1.0.0    | [BSD-3-Clause](https://opensource.org/license/BSD-3-Clause) |            Manages environment variables            |
|        pytz         |   2023.3    |          [MIT](https://opensource.org/license/MIT)          |                Timezone conversions                 |
|      requests       |   2.31.0    |  [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)  |          Handles HTTP requests to the API           |
|   timezonefinder    |    6.5.9    |          [MIT](https://opensource.org/license/MIT)          |         Detects timezones with coordinates          |
|       urllib3       |    2.4.0    |          [MIT](https://opensource.org/license/MIT)          |                    Handles URL's                    |

## Legal and Ethical Requirements

- All libraries and packages are used in accordance with their respective license requirements, which can be found hyperlinked in the table above.
- Use of the OpenWeatherMap API is in accordance with its [terms and conditions](https://openweather.co.uk/storage/app/media/Terms/Openweather_terms_and_conditions_of_sale.pdf)
- API usage is limited to 60 requests per minute
- CSV and JSON files created by the app are only stored locally in the root folder

## Security Impacts

| **Package/Library** |        **Potential Risks**         |                                            **Mitigation Used**                                            |
| :-----------------: | :--------------------------------: | :-------------------------------------------------------------------------------------------------------: |
|      Requests       |  API hijacking, data interception  |                                 Uses HTTPS with certificate verification                                  |
|        Numpy        | Numeric processing vulnerabilities |                                     Only used through timezonefinder                                      |
|       Urllib3       |       HTTP header injection        | Patched in current version (2.4+), used through requests, code to reject special characters as city names |

# CLI Weather Application - Fetch Current Weather

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
   - [Linux/WSL/Mac](#linuxwslmac)
   - [Windows CMD](#windows)
5. [Using the App](#using-the-app)
6. [Additional Information](#additional-information)
7. [Files](files)
8. [External Libraries\Packages](#external-librariespackages)
9. [Legal and Ethical Requirements](#legal-and-ethical-requirements)
10. [Security Impacts](#security-impacts)
11. [Troubleshooting](#troubleshooting)
12. [Testing](#testing)

## Overview

This is a python command line application that gives you current weather data for any capital city in the world!

The application will output current temperature, humidity, weather conditions and local time of the last weather update.

When selecting cities with shared names, add the ISO 3166 state and country code, (e.g. "melbourne nsw au"). The state code is not always needed unless city name exists more than once in the same country.

Words can be separated with commas or spaces

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
- [Windows CMD](#windows)

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
   - Create a file named .env in the project root and save your API key as `OWM_API_KEY = "api-key-here"`
   - Verify email address used with confirmation email - API KEY WILL NOT WORK IF YOU SKIP THIS STEP!!!
   - The API key can take a few minutes to activate, for testing purposes only the following pre-confirmed API key can be used - "0c3330fa568c970e539a75c0d5c08c40"
   - NOTE - In a normal deployment setting, the use of a pre-provided API key could constitute a security risk and is only used here to expedite the testing process.

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

**_Use CMD not Powershell_**

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
   - Create a file named .env in the project root and save your API key as `OWM_API_KEY = "api-key-here"`
   - Verify email address used with confirmation email - API KEY WILL NOT WORK IF YOU SKIP THIS STEP!!!
   - The API key can take a few minutes to activate, for testing purposes only the following pre-confirmed API key can be used - "0c3330fa568c970e539a75c0d5c08c40"
   - NOTE - In a normal deployment setting, the use of a pre-provided API key could constitute a security risk and is only used here to expedite the testing process.

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

## Using the App

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
- Pre provided API Key is for testing by CoderAcademy staff only and would not be present in normal deployment

## Security Impacts

| **Package/Library** |        **Potential Risks**         |                                            **Mitigation Used**                                            |
| :-----------------: | :--------------------------------: | :-------------------------------------------------------------------------------------------------------: |
|      Requests       |  API hijacking, data interception  |                                 Uses HTTPS with certificate verification                                  |
|        Numpy        | Numeric processing vulnerabilities |                                     Only used through timezonefinder                                      |
|       Urllib3       |       HTTP header injection        | Patched in current version (2.4+), used through requests, code to reject special characters as city names |

## Troubleshooting

|                   **Error Message**                    |                              **Cause**                               |                                                                                                                       **Solution**                                                                                                                       |
| :----------------------------------------------------: | :------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|          Error: Missing API key in .env file           |                  Missing or invalid format API key                   |                                                  Refer to installation instructions and check that API key is appropriately installed in .env file in root directory as `OWM_API_KEY = "api-key-here"`                                                   |
|             HTTP Error: 401 - Unauthorized             |               API Key invalid or incorrectly formatted               | New API keys can take time to be validated. Ensure the email address for your OpenWeatherMap account is verified, and that formatting matches as described above and in API installation instructions. Refer to default API key provided if still faulty |
|  "Error: Unable to connect to the OpenWeatherMap API"  |                      Faulty internet connection                      |                                                                                                            Ensure active internet connection                                                                                                             |
|         Error: Request timed out (10 seconds)          |     Server overload, network issues DNS issues, Firewall issues      |                                                                  Test internet connection, test api url in browser, and if no problems in browser check firewall and security settings                                                                   |
|             "HTTP Error: 404 - Not Found"              | User has entered an incorrect city name OR API link has broken/moved |                                                                                      Try with valid city name, test API URL in browser to see if link still active                                                                                       |
| Value Error: Expecting value: line 1 column 1 (char 0) |              Request has failed to return weather data               |                                                                                                      Check valid city name, test API URL in browser                                                                                                      |

## Testing

### 1. Unit Testing

For testing of correct function output for the `dt_conversion.py` module using Pytest.
From the activated virtual environment, run the following command:

```bash
PYTHONPATH=src pytest tests/test_dt_conversion.py
```

If greater detail required from test results, add `--tb=long -vv` after pytest.

Depreciation warning for `datetime.datetime.utcfromtimestamp()` is already known and accounted for.

### 2. Integration Testing

For testing of correct API/HTTP error handling of `weather_service.py`, without calling external API, using the requests-mock library and Pytest.
From the activated virtual environment, run the following command:

```bash
PYTHONPATH=src pytest tests/test_weather_service.py
```

If greater detail required from test results, add `--tb=long -vv` after pytest.

### 3. CLI Integration Testing

For testing user interaction with the CLI, ensuring that the app responds as expexted to various inputs, and that it outputs as expected given certain inputs.

From the activated virtual environment, run the following command:

```bash
PYTHONPATH=src pytest tests/test_main_cli.py
```

If greater detail required from test results, add `--tb=long -vv` after pytest.

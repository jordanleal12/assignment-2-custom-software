""" Converts raw unix timestamp to local timezone aware datetime """

from datetime import datetime # Used to format the date and time
import pytz # Used to handle timezone conversions
from timezonefinder import TimezoneFinder # Used to find timezone based on latitude and longitude

def get_timezone(coords: dict) -> str:
    """Get the timezone name based on latitude and longitude."""

    try: # Create a TimezoneFinder instance
        # Check if the coordinates dictionary contains "lat" and "lon" keys
        if "lat" not in coords or "lon" not in coords:
            raise ValueError("Coordinates must contain 'lat' and 'lon' keys.")
        # Get the timezone name from latitude and longitude
        timezone_name = TimezoneFinder().timezone_at(lat=coords["lat"], lng=coords["lon"])
        # If timezone isn't found, raise an error as timezone_name will be None
        if not timezone_name: # If timezone_name is None, it means the coordinates are invalid
            raise ValueError("Coordinates do not correspond to a valid timezone.")
        return timezone_name
    except ValueError as e:
        # Handle any exceptions that occur during timezone lookup, revert to UTC
        print(f"Error getting timezone: {e}, reverting to UTC.")
        return "UTC"

def convert_time(unix_dt: int, coords: dict) -> str:
    """Convert Unix timestamp to local time in the specified timezone."""

    # Convert naive timestamp to (UTC) timezone aware datetime object
    utc_dt = datetime.fromtimestamp(unix_dt, tz=pytz.utc)
    # Create local timezone object from the city coordinates using get_timezone function
    local_tz = pytz.timezone(get_timezone(coords))
    # Convert UTC datetime to local timezone
    local_dt = utc_dt.astimezone(local_tz)
    # Return formatted local datetime as a string
    return local_dt.strftime("%d-%b-%y %I:%M %p %Z")

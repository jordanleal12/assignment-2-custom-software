""" Converts raw unix timestamp to local timezone aware datetime """

from datetime import datetime # Used to format the date and time
import pytz # Used to handle timezone conversions
from timezonefinder import TimezoneFinder # Used to find timezone based on latitude and longitude

def get_timezone(coords: dict) -> str:
    '''Get the timezone name based on latitude and longitude.'''
    # Create a TimezoneFinder instance
    tf = TimezoneFinder()
    # Get the timezone name from latitude and longitude
    timezone_name = tf.timezone_at(lat=coords["lat"], lng=coords["lon"])
    return timezone_name

def convert_time(unix_dt: int, coords: dict) -> str:
    '''Convert Unix timestamp to local time in the specified timezone.'''
    # Convert naive timestamp to (UTC) timezone aware datetime object
    utc_dt = datetime.fromtimestamp(unix_dt, tz=pytz.utc)
    # Create local timezone object from the city coordinates using get_timezone function
    local_tz = pytz.timezone(get_timezone(coords))
    # Convert UTC datetime to local timezone
    local_dt = utc_dt.astimezone(local_tz)
    # Return formatted local datetime as a string
    return local_dt.strftime("%d-%b-%y %I:%M %p %Z")

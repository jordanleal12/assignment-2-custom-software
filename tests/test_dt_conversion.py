"""Test cases for the dt_conversion module."""

# import pytz
# import pytest
import dt_conversion as dtc


def test_get_timezone_missing_keys(capsys):
    """Passing no keys should print an error and return 'UTC'"""

    tz = dtc.get_timezone({})
    captured = capsys.readouterr()
    assert "Coordinates must contain 'lat' and 'lon'" in captured.out
    assert tz == "UTC"

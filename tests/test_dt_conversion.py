"""Test cases for the dt_conversion module. PYTHONPATH=src must be input in terminal to run this file."""

# import pytz
# import pytest
import dt_conversion as dtc


def test_get_timezone_missing_keys(capsys):
    """Passing no keys should print an error and return 'UTC'"""

    tz = dtc.get_timezone({})
    captured = capsys.readouterr()
    assert "Coordinates must contain 'lat' and 'lon'" in captured.out
    assert tz == "UTC"

def test_get_timezone_invalid_coords(capsys, monkeypatch):
    """Passing invalid coordinates should print an error and return 'UTC'"""

    class DummyTF:
        """Dummy TimezoneFinder class to return none."""
        def timezone_at(self, lat, lng):
            """Return None for any coordinates."""
            return None
    monkeypatch.setattr(dtc, "TimezoneFinder", lambda: DummyTF())

    tz = dtc.get_timezone({"lat": 0, "lon": 0})
    captured = capsys.readouterr()
    assert "Coordinates do not correspond to a valid timezone" in captured.out
    assert tz == "UTC"

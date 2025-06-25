"""Test cases for dt_conversion module. Refer to 'Testing' in Readme for instructions."""

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

def test_convert_time(monkeypatch):
    """Test that convert_time converts unix timestamp to expected datetime given timezone."""
    # Make get_timezone always return "UTC"
    monkeypatch.setattr(dtc, "get_timezone", lambda coords: "UTC")
    # 1609459200 = 2021-01-01 00:00:00 UTC
    result = dtc.convert_time(1609459200, {"lat": 0, "lon": 0})
    # Format is "%d-%b-%y %I:%M %p %Z", so we expect: 01-Jan-21 12:00 AM UTC
    assert result == "01-Jan-21 12:00 AM UTC"

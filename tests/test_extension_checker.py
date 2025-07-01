import pytest
from main import extension_checker

def test_adds_missing_extension():
    # GIVEN a filename without “.csv”
    filename = "data"
    # WHEN I run extension_checker
    result = extension_checker(filename, ".csv")
    # THEN it should tack on “.csv”
    assert result == "data.csv"


def test_replaces_wrong_extension():
    # GIVEN a filename ending in .txt but I want .json
    filename = "report.txt"
    # WHEN I run extension_checker
    result = extension_checker(filename, ".json")
    # THEN it should swap to .json
    assert result == "report.json"
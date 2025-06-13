import pytest

from calculator import StringCalculator


def test_empty_string_input():
    """
    Test the StringCalculator with an empty string input.
    This should return 0 as per the specification.
    """
    calc = StringCalculator()
    assert calc.add("") == 0, "Expected 0 for empty string input"


def test_single_number_input():
    """
    Test the StringCalculator with a single number input.
    This should return the number itself if it's a valid digit,
    or 0 if it's a special symbol.
    """
    calc = StringCalculator()
    assert calc.add("5") == 5, "Expected 5 for single number input"
    assert calc.add("?") == 0, "Expected 0 for single special symbol input"
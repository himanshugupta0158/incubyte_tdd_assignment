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


def test_two_numbers_input():
    """
    Test the StringCalculator with two numbers input.
    This should return the sum of the two numbers if both are valid digits or numbers,
    or the first number if the second is a special symbol and vice versa
    else return 0 incase both are non-numeric strings.
    """
    calc = StringCalculator()
    assert calc.add("3,4") == 7, "Expected 7 for input '3,4'"
    assert calc.add("10,20") == 30, "Expected 30 for input '10,20'"
    assert calc.add("5,?") == 5, "Expected 5 for input '5,?'"

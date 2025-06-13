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


def test_multiple_numbers_input():
    """
    Test the StringCalculator with multiple numbers input.
    This should return the sum of all valid numbers in the string.
    """

    calc = StringCalculator()
    assert calc.add("1,2,3") == 6, "Expected 6 for input '1,2,3'"
    assert calc.add("10,20,30") == 60, "Expected 60 for input '10,20,30'"
    assert calc.add("5,?,7") == 12, "Expected 12 for input '5,?,7'"
    assert calc.add("?,10,20") == 30, "Expected 30 for input '?,10,20'"
    assert calc.add("?,?,?") == 0, "Expected 0 for input '?,?,?'"
    nums = ",".join(["2" for i in range(10)])
    assert calc.add(nums) == 20, f"Expected 20 for input '{nums}'"


def test_invalid_input():
    """
    Test the StringCalculator with invalid input.
    This should return 0
    """
    calc = StringCalculator()
    assert calc.add("a,b,c") == 0, "Expected 0 for input 'a,b,c'"
    assert calc.add("1,2,a") == 3, "Expected 3 for input '1,2,a'"
    assert calc.add("?") == 0, "Expected 0 for single special symbol input"
    assert calc.add("?,?") == 0, "Expected 0 for two special symbols input"


def test_new_lines_as_delimiters():
    """
    Test the StringCalculator with new lines as delimiters.
    This should return the sum of the numbers separated by new lines.
    """
    calc = StringCalculator()
    assert calc.add("1\n2\n3,4") == 10, "Expected 10 for input '1\\n2\\n3,4'"
    assert calc.add("10\n20\n30") == 60, "Expected 60 for input '10\\n20\\n30'"
    assert calc.add("5\n?\n7") == 12, "Expected 12 for input '5\\n?\\n7'"
    assert calc.add("?,10\n20") == 30, "Expected 30 for input '?,10\\n20'"
    assert calc.add("?,?\n?") == 0, "Expected 0 for input '?,?,?'"


def test_custom_delimiters():
    """
    Test the StringCalculator with custom delimiters.
    This should return the sum of the numbers separated by custom delimiters.
    """
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3, "Expected 3 for input '//;\\n1;2'"
    assert calc.add("1;2;3,4") == 10, "Expected 10 for input '1;2;3,4'"
    assert calc.add("10;20;30") == 60, "Expected 60 for input '10;20;30'"
    assert calc.add("5;?;7") == 12, "Expected 12 for input '5;?;7'"
    assert calc.add("?,10;20") == 30, "Expected 30 for input '?,10;20'"
    assert calc.add("?,?;?") == 0, "Expected 0 for input '?,?,?'"

def test_negative_numbers():
    """
    Test the StringCalculator with negative numbers.
    This should raise a ValueError with the appropriate message.
    """
    calc = StringCalculator()
    with pytest.raises(ValueError) as exc_info:
        calc.add("-1,-2")
    assert str(exc_info.value) == "negative numbers not allowed -1, -2", "Expected ValueError for negative numbers"

    with pytest.raises(ValueError) as exc_info:
        calc.add("5,-3,2")
    assert str(exc_info.value) == "negative numbers not allowed -3", "Expected ValueError for negative numbers"
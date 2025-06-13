import pytest

from calculator import StringCalculator


def test_empty_string_input():
    calc = StringCalculator()
    assert calc.add("") == 0, "Expected 0 for empty string input"

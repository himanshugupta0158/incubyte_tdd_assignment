import re


class StringCalculator:
    """
    A simple string calculator that can add numbers from a string input.
    It supports empty strings, single numbers, and comma-separated numbers.
    The calculator ignores special symbols and returns 0.
    """

    def add(self, numbers: str):
        if not numbers:
            return 0

        numbers = self.__extract_numbers(numbers)
        return self.__sum_numbers(numbers)

    def __extract_numbers(self, numbers: str):
        return re.findall(r"\d+", numbers)

    def __sum_numbers(self, numbers: list):
        total = 0
        for num in numbers:
            total += int(num)
        return total

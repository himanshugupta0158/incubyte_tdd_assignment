from typing import Union


class StringCalculator:
    """
    A simple string calculator that can add numbers from a string input.
    It supports empty strings, single numbers, and comma-separated numbers.
    """

    def add(self, numbers: str):
        if not numbers:
            return 0

        numbers = self.__split_numbers(numbers)
        return self.__sum_numbers(numbers)

    def __split_numbers(self, numbers: str):
        if "," in numbers:
            return numbers.split(",")
        return int(numbers) if numbers.isdigit() else 0

    def __sum_numbers(self, numbers: Union[int, list]):
        if isinstance(numbers, int):
            return numbers
        if isinstance(numbers, list):
            total = 0
            for number in numbers:
                if number.isdigit():
                    total += int(number)
            return total
        return 0

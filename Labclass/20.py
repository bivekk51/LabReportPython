import math

class NegativeNumberError(Exception):
    def __init__(self, number, message="Square root of a negative number is not defined."):
        self.number = number
        self.message = message
        super().__init__(self.message)

def sqrt(number):
    if number < 0:
        raise NegativeNumberError(number)
    return math.sqrt(number)

try:
    result = sqrt(-9)
    print(f"The square root is: {result}")
except NegativeNumberError as e:
    print(f"Error: {e}. Number passed: {e.number}")

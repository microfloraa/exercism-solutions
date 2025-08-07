"""Function to determine whether a submitted number is an Armstrong number."""


def is_armstrong_number(number):
    """Determine whether a submitted number is an Armstrong number.

    :param number: int - number to be tested.
    """

    num_str = str(number)
    power = len(num_str)
    digits = [int(digit) for digit in num_str]

    result = [digit**power for digit in digits]
    if sum(result) == number:
        return True
    return False
    
    
   

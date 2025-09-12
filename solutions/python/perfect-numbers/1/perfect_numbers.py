"""Function to classify numbers based on Nicomachus' scheme."""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    
    factors = []
    count = 1
    while count < number:
        if number % count == 0: factors.append(count)
        count = count + 1

    if number == sum(factors): return 'perfect'
    if number < sum(factors): return 'abundant'
    if number > sum(factors): return 'deficient'

"""Function to classify numbers based on Nicomachus' scheme."""


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: 
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = []
    for i in range(1, number):
        if number % i == 0: 
            factors.append(i)

    if number == sum(factors):
        return 'perfect'
    if number < sum(factors):
        return 'abundant'
    return 'deficient'

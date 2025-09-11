"""Function to convert a number to raindrop noises."""

def convert(number):
    """Convert a number to raindrop noises.
    
    :param number: int - number to convert.
    :result: str - raindrop noises.
    """
    result = []
    if number % 3 == 0: result.append('Pling')
    if number % 5 == 0: result.append('Plang')
    if number % 7 == 0: result.append('Plong')
    if result == []: result.append(str(number))

    return ''.join(result)
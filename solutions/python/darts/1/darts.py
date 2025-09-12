"""Function to score a dart throw."""

def score(x, y):
    """Determine score of throw based on where dart landed on dartboard.
    
    :param x: int - x coordinate of throw.
    :param y: int - y coordinate of throw.
    :result: int - score of throw.

    The radius of the dartboard is 10 and coordinates (0, 0) are the center.
    """
    hypotenuse = (abs(x) ** 2) + (abs(y) ** 2)

    if 0 <= hypotenuse <= 1: return 10
    if 1 < hypotenuse <= 25: return 5
    if 25 < hypotenuse <= 100: return 1
    return 0
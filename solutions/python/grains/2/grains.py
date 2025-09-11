"""Functions to calculate the number of grains of wheat on a chessboard."""


def square(number):
    """Calculate the number of wheat grains on a given square.

    :param number: int - square on chessboard.
    :return: int - number of wheat grains on given square.
    """
    if 1 <= number <= 64: return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Calculate the total number of wheat grains.
    
    :return: int - total number of wheat grains.
    """
    return (2 ** 64) - 1
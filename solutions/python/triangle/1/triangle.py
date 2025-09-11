"""Functions for determining if a triangle is equilateral, isosceles, or scalene."""


def valid_triangle(sides):
    """Determine if the given lengths can form a valid triangle.
    
    :param sides: list - of lengths to evaluate.
    :return: bool - is valid triangle?
    """
    if any(sides) == 0: return False
    if sides[0] + sides[1] < sides[2]: return False
    if sides[0] + sides[2] < sides[1]: return False
    if sides[1] + sides[2] < sides[0]: return False
    return True


def equilateral(sides):
    """Determine if the given lengths form an equilateral triangle.
    
    :param sides: list - of lengths to evaluate.
    :return: bool - is equilateral triangle?
    """
    if valid_triangle(sides) is True: return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    """Determine if the given lengths form an isosceles triangle.
    
    :param sides: list - of lengths to evaluate.
    :return: bool - is isosceles triangle?
    """
    if valid_triangle(sides) is True: return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return False


def scalene(sides):
    """Determine if the given lengths form a scalene triangle.
    
    :param sides: list - of lengths to evaluate.
    :return: bool - is scalene triangle?
    """
    if valid_triangle(sides) is True: return sides[0] != sides[1] != sides[2] != sides[0]
    return False
def steps(number):
    """Calculate the number of steps needed to reach 1.

    :param number: int - any positive integer.
    :return: int - the number of operations needed to reach 1.

    Function that takes a positive integer as an argument and returns
    the number of operations needed to reach 1 using the Collatz Conjecture.
    """
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    working_number = number
    step_count = 0
    
    while working_number > 1:
        if working_number % 2 == 0:
            working_number = working_number / 2
            step_count = step_count + 1
        else:
            working_number = (working_number * 3) + 1
            step_count = step_count + 1

    return step_count

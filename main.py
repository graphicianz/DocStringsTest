import doctest

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.

    Examples:
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-10, 5)
    -5
    >>> add_numbers(0, 0)
    0
    """
    return a + b

if __name__ == '__main__':
    doctest.testmod()
"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    add_nums = float(num1 + num2)

    return add_nums


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    subtract_nums = float(num2 - num1)

    return subtract_nums


def multiply(num1, num2):
    """Multiply the two inputs together."""
    multiply_nums = float(num1 * num2)

    return multiply_nums


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divide_nums = float(num2 / num1)

    return divide_nums


def square(num1):
    """Return the square of the input."""
    square_num = float(num1**num1)

    return square_num


def cube(num1):
    """Return the cube of the input."""
    cube_nums = float(num1**3)

    return cube_nums


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power_num = float(num1**num2)

    return power_num


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mod_nums = float(num1 % num2)

    return mod_nums
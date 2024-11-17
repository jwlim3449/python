def factorial(n):
    """
    Calculate the factorial of a given number n recursively.

    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage
number = 10
result = factorial(number)
print(f"The factorial of {number} is {result}")

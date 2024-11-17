def calculator(a, b, operation):
    """
    Perform basic arithmetic operations.

    :param a: First number
    :param b: Second number
    :param operation: Operation ('add', 'subtract', 'multiply', 'divide')
    :return: Result of the operation
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "Cannot divide by zero!"
        return a / b
    else:
        return "Invalid operation!"


# Example usage
print("Addition:", calculator(5, 3, 'add'))
print("Division:", calculator(10, 0, 'divide'))


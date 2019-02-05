
print('This program calculates the nth term of the fibonacci series.')
print('-----')


def fibonacci(nth):
    """Calculate the nth term of the fibonacci series."""

    total = 0  # initial value of the sum
    for i in range(0, nth+1):  # obtain the wanted sum (fibonacci series)
        total += i

    return total


# -- Main program
nth = int(input('Introduce nth term: '))
print('Value =', fibonacci(nth))

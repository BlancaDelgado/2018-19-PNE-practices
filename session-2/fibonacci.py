
print('-----')
print('This program calculates the nth term of the fibonacci series.')
print('-----')


def fibonacci(nth):
    """Calculate the nth term (of positive integers) of the fibonacci series."""


    if type(nth) is not int or nth < 0:
        print('ERROR: Please introduce a positive integer.')
        return False

    elif 0 <= nth <= 1:
        return nth

    else:
        first = 0; second = 1
        for i in range(0, nth-2):  # obtain the wanted sum (fibonacci series)
            sol = first + second

            # UPDATE VALUES
            second = first
            first = sol

        return sol


# -- Main program
nth = int(input('Introduce nth term: '))
print('Value =', fibonacci(nth))

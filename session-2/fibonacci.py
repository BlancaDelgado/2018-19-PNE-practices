print('-----')
print('This program calculates the nth term of the fibonacci series.')
print('-----\n')

def fibonacci(nth):
    """Calculates the nth term of the fibonacci series."""

    if nth < 0:
        print('ERROR: Please introduce a positive integer.\n')
        return None

    elif nth == 0 or nth == 1:
        sol1 = nth
        return sol1

    elif nth > 1:

        first = 0
        second = 1
        for i in range(0, nth-1):
            sol2 = first + second

            first = second
            second = sol2

        return sol2

    else:
        print('ERROR: Sorry, the program could not find an answer for your term.')
        return None


# -- Main program

nth = int(input('Introduce nth term: '))
print('Value =', fibonacci(nth))

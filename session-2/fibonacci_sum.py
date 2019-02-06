print('-----')
print('This program calculates the sum of the first nth terms of the fibonacci series.')
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

def fibo_sum(nth):

    if nth < 0:
        print('ERROR: Please introduce a positive integer.\n')
        return None

    elif nth == 0:
        print('Solution = 0 (you haven\'t added anything!')
        return None

    elif nth > 0:

        # Add each previous element AND the selected element
        sol_sum = 0
        for i in range(0, nth+1):
            element = fibonacci(i)
            sol_sum += element

        return sol_sum

    else:
        print('ERROR: Sorry, the program could not work out your answer!\n')
        return None


# -- Main program
nth = int(input('Introduce the nth element: '))
print('Solution:', fibo_sum(nth))

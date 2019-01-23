print('This program sums the first n integers. ')


def sumn(n):

    total = 0
    for i in range(n):
        total += i + 1

    return total


# -- Main program
num = int(input('Choose the number of integers to add them up: '))
total_sum = sumn(num)
print('The total sum is {}'.format(total_sum))

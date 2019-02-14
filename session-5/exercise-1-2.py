# Program that calls 'count_bases()' from 'Bases.py'

# IMPORT FUNCTION FROM ANOTHER FILE
from Bases import count_bases

# --Main program from 'exercise-1.py'

# ASK USER FOR SEQUENCE
s = input('Please enter the sequence: ')

print('\n----------INFORMATION ABOUT SEQUENCE----------')

# PRINT TOTAL LENGTH
total_length = len(s)
print('\nThis sequence is', total_length, 'bases in length.')

# PRINT NUMBER OF BASES AND PERCENTAGE
for base in 'ATCG':
    print('\nBase', base)

    counter = count_bases(s)[base]
    print('- Counter:', counter)

    try:
        perc = round(100.0 * counter / total_length, 1)
    except ZeroDivisionError:
        perc = 0
    print('- Percentage: {}%'.format(perc))



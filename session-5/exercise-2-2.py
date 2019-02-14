# Program that calls 'count_bases()' from 'Bases.py'

# IMPORT FUNCTION FROM ANOTHER FILE
from Bases import count_bases

# --Main program from 'exercise-2.py'

# --Main program

# ASK USER FOR TWO SEQUENCES
s1 = input('Please enter the first sequence: ')
s2 = input('Please enter the second sequence: ')

sequences = [s1, s2]  # save sequences in a list

num_seq = 0
for s in sequences:
    num_seq += 1
    print('\n---------- INFORMATION ABOUT SEQUENCE', num_seq, '----------')

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

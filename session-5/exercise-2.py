# Modified 'exercise-1.py' for counting all bases of two sequences introduced by the user.


def count_bases(seq):
    """ Counts all bases (A, T, C, G).

        -----
        Returns a dictionary with four entries."""

    dict_bases = {}  # empty dictionary {base:counter}

    # COUNT BASES, ONE AT A TIME!
    for base in 'ACGT':

        num_bases = 0
        for element in seq:  # check how many bases are in the sequence

            if element == base:
                num_bases += 1

        dict_bases.update({base: num_bases})

    return dict_bases


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

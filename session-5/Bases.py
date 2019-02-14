# Moved function from exercises 1 and 2.

def count_bases(seq):
    """
    Counts all bases (A, T, C, G).

    -----
    Returns: dictionary with four entries.
    """

    dict_bases = {}  # empty dictionary {base:counter}

    # COUNT BASES, ONE AT A TIME!
    for base in 'ACGT':

        num_bases = 0
        for element in seq:  # check how many bases are in the sequence

            if element == base:
                num_bases += 1

        dict_bases.update({base: num_bases})

    return dict_bases

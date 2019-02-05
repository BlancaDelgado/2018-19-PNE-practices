def count_a(seq):
    """Counting the number of As in the sequence."""

    # Counter fro the As
    result = 0

    for b in seq :
        if b == 'A':
            result += 1

    # Result the result
    return result

# Main program
s = 'AGTACACATTA'

na = count_a(s)
print('The number of As is: {}'.format(na) )
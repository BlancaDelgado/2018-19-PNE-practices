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

# Calculate the total sequence length
tl = len(s)

# Calculate the percentage of As in the sequence
perc = round(100.0 * na / tl, 1)

print('The total length is: {}'.format(tl))
print('The percentage of As is: {}%.'format(perc))


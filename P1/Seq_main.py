# Main program that creates four sequences

# FROM DOCUMENT, IMPORT CLASS
from Seq import Seq

# CREATE CLASSES FOR FIRST TWO SEQ
# From this two classes, we will create all sequences
Seq_1 = Seq('AGTACACTGGT')
Seq_2 = Seq('CGTAAC')

# CREATE THE FOUR SEQUENCES
s1 = Seq_1.strbase  # invoking seq method directly
s2 = Seq_2.strbase  # invoking seq method directly
s3 = Seq_1.complement()  # complement of first one
s4 = Seq_1.reverse()  # reverse of third sequence

sequences = (s1, s2, s3, s4)  # tuple with all seqs

# GIVE INFORMATION OF SEQUENCES
num = 0
for sequence in sequences:
    num += 1
    Seq_n = Seq(sequence)
    print()
    print('--------------------- SEQUENCE', num, '---------------------')

    # Print sequence string
    print('Sequence {}'.format(num) + ': {}'.format(sequence))

    # Print total length
    print('\tLength: {}'.format(Seq_n.len()))

    # Calculate bases count and percentage
    counting_b = []
    counting_perc = []
    for b in 'ATCG':
        counting_b.append(b + ':')
        counting_b.append('{}'.format(Seq_n.count(b)) + ' ')

        counting_perc.append(b + ':')
        counting_perc.append('{}%'.format(Seq_n.perc(b)) + ' ')

    # Print number of bases of every type
    counter_b = ''.join(counting_b)
    print('\tBases count: ' + counter_b)

    # Print percentage of bases of every type
    counter_perc = ''.join(counting_perc)
    print('\tBases percentage: ' + counter_perc)

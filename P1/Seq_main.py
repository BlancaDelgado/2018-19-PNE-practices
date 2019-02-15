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
for sequence in sequences:
    print(sequence)





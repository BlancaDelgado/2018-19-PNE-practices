print('-----')
print('This program counts the number of basis (A, C, G, T) of the sequence CPLX2 saved in its file.')
print('-----\n')

# -- Main program

# Open the document
with open('CPLX2.txt', 'r') as file:
    rfile = file.read()
    file.close()

# Clean the sequence
seq = rfile.split('\n')

for line in seq:

    if line.startswith('>'):
        seq.remove(line)

clean_seq = ''.join(seq)

# Count the basis
for base in 'ACGT':
    print('Number of', base, ':', clean_seq.count(base))

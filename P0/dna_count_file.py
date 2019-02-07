print('-----')
print('This program counts the number of basis and the total length of a DNA sequence from an external file.')
print('-----\n')

def num_basis(base, seq):

    if base in 'ACGT':
        sol = seq.count(base)
        return sol

    else:
        print('ERROR: This is not a base of DNA sequences. Choose A, C, G or T.')
        return None


#-- Main program

# Open file and save the content in a variable
with open('basis.txt', 'r') as file:

    rfile = file.read()
    file.close()

# Clean the content
seq = rfile.replace('\n', '').upper()

# Workout the functions
print('TOTAL LENGTH ----- ', len(seq))

for base in 'ACGT':
    print('Total number of', base, ': ', num_basis(base, seq))

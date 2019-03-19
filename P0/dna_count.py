print('-----')
print('This program counts the number of basis presented in a DNA sequence and its total length')
print('-----\n')

def num_basis(base, seq):

    if base in 'ACGT':
        sol = seq.count(base)
        return sol

    else:
        print('ERROR: This is not a base of DNA sequences. Choose A, C, G or T.')
        return None


#-- Main program
seq = input('Introduce DNA sequence: ').upper()

print()
print('TOTAL LENGTH ----- ', len(seq))

for base in 'ACGT':
    print('Total number of', base, ': ', seq.count(base))

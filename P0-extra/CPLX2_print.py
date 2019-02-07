print('-----')
print('This program open a file that contains a gene sequence and prints its data.')
print('-----\n')

with open('CPLX2.txt', 'r') as file:
    rfile = file.read()
    file.close()

print(rfile)

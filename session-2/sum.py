print('This program sums up the first 100 integer numbers.')

total_sum = 0
for i in range(0,101): # Add until 100, range doesn't count with last value.
    total_sum += i

print('Final count:', total_sum)
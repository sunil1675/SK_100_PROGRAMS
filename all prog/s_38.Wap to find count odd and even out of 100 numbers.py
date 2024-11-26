#Program by SUNIL SIR
#38.Wap to find count odd and even out of 100 numbers.

print('38.Wap to find count odd and even out of 100 numbers.\n')
import random
l=[random.randint(1,100) for i in range(10)]
print(f'List: {l}')

e=0
o=0
for i in l:
    if i%2==0:
        e=e+1
    else:
        o=o+1


print(f'\nNo. of even numbers in the list is {e}')
print(f'No. of odd numbers in the list is {o}')
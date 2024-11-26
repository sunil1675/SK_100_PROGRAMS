'''program by SUNIL SIR
52.Wap to count number of negative numbers and positive numbers, odd and even number from a list of numbers. The list terminates the num entered zero.'''

print('''52.Wap to count number of negative numbers and positive numbers, odd and even number
   from a list of numbers. The list terminates the num entered zero.\n''')

import random
l=[random.randint(-100,100) for i in range(10)]
print(f'List: {l}')

n=0
p=0
e=0
o=0

for i in l:
    if i==0:
        pass

    if i>0:
        p=p+1

    elif i<0:
        n=n+1


    if i%2==0:
        e=e+1

    else:
        o=o+1

print(f'\nNo. of positive numbers in the list is {p}')
print(f'No. of negative numbers in the list is {n}')
print(f'\nNo. of even numbers in the list is {e}')
print(f'No. of odd numbers in the list is {o}')
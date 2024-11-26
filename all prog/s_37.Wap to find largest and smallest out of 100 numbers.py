#program by SUNIL SIR
#37.Wap to find largest and smallest out of 100 numbers.

print('37.Wap to find largest and smallest out of 100 numbers.\n')
import random
l=[random.randint(1,100) for i in range(10)]

print(f'List: {l}')
m=max(l)
s=min(l)
print(m,s)
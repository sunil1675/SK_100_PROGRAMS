#program by SUNIL SIR
#86.Wap to reverse a vector without using a temporary variable.

print('86.Wap to reverse a vector without using a temporary variable.')

import random
a=[random.randint(1,100) for i in range(11)]

print(f'\n\nOriginal vector: {a}')
a=a[::-1]
print(f'\nReversed vector: {a}')
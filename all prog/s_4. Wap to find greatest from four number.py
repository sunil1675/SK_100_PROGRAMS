#Program by SUNIL SIR
#4. Wap to find greatest from four number.

print('4. Wap to find greatest from four number.\n ')

a=int(input('Enter First No.'))
b=int(input('Enter Second No.'))
c=int(input('Enter Third No.'))
d=int(input('Enter Fourth No.'))

if a>b and a>c and a>d:
    print(f'\n{a} is greater than {b}, {c} & {d}')
elif b>a and b>c and b>d:
    print(f'\n{b} is greater than {a}, {c} & {d}')
elif c>a and c>b and c>d:
    print(f'\n{c} is greater than {a}, {b} & {d}')
else:
    print(f'\n{d} is greater than {a}, {b} & {c}')

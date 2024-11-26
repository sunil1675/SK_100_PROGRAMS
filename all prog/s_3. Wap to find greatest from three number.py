#Program by SUNIL SIR
#3. Wap to find greatest from three number.

print('3. Wap to find greatest from three number.\n ')

a=int(input('Enter First No.'))
b=int(input('Enter Second No.'))
c=int(input('Enter Third No.'))

if a>b and a>c:
    print(f'\n{a} is greater than {b} and {c}')
elif b>a and b>c:
    print(f'\n{b} is greater than {a} and {c}')
else:
    print(f'\n{c} is greater than {a} and {b}')

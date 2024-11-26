#program by SUNIL SIR
#49.Wap to read two number and swap their values(without using third variable )

print('49.Wap to read two number and swap their values(without using third variable )')

a=int(input('ENTER VALUE OF A: '))
b=int(input('ENTER VALUE OF B: '))

a=a+b
b=a-b
a=a-b

print(f'\nSwapping the values of A & B \nA= {a}\nB= {b}')
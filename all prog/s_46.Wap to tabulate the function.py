'''#program by SUNIL SIR
#46.Wap to tabulate the function
    F(x)=(x**2 +1.5x+5)/(x-3)
    For x = -10 to 10, x should take values –10 –8 –6…6,8,10
'''

l=list(range(-10,11,2))

print(' x  |     F(x)')
print('-------------')

for x in l:
    if x==3:
        print(f'{x:2} |     Undefined')
    else:
        Fx=(x**2+1.5*x+5)/(x-3)
        print(f"{x:2} |     {Fx:10.2f}")
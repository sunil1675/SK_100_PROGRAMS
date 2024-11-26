#program by SUNIL SIR
#51.Wap to generate divisors of an integer.

print('51.Wap to generate divisors of an integer.\n')

n=int(input('Enter the integer: '))

print(f"\nDivisors of {n}:",end=' ')

for i in range(1,n+1):
    if n%i==0:
        print(i,end=',')
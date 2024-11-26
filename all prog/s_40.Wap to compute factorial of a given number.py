#program by SUNIL SIR
#40.Wap to compute factorial of a given number

print('40.Wap to compute factorial of a given number.\n')

n=int(input('Enter a no. to get the factorial of: '))

f=1
for i in range(1,n+1):
    f=f*i
print(f'FACTORIAL OF {n} IS: {f}')
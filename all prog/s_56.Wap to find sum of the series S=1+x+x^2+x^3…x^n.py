#program by SUNIL SIR
#56.Wap to find sum of the series S=1+x+x**2+x**3…x**n

print('56.Wap to find sum of the series S=1+x+x**2+x**3…x**n.\n')

x=int(input('Enter x: '))
n=int(input('Enter n: '))
s=0
for i in range(n+1):
    s=s+(x**i)
print('SUM:',s)
#program by SUNIL SIR
#45.Wap to print first n natural numbers and their sum.

print('''45.Wap to print first n natural numbers and their sum.\n''')
print('''#1+2+3+.......+n \n ''')
n=int(input('Enter value of n: '))
s=0
for i in range (1,n+1):
    s=s+i
print('Sum:',s)
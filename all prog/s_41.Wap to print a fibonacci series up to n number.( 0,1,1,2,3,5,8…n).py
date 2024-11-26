'''Program by SUNIL SIR
41.Wap to print a fibonacci series up to n number.( 0,1,1,2,3,5,8…n)'''

print('41.Wap to print a fibonacci series up to n number.( 0,1,1,2,3,5,8…n)\n')

n=int(input('Enter a number to print fibonacci seqence upto: '))
print()
a=0
b=1
print(a,b,end=',')

for i in range(n-2):
    c=a+b
    print(c,end=',')
    a=b
    b=c
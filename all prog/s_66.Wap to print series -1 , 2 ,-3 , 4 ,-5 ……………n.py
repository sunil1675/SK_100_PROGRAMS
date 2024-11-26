#program by SUNIL SIR
#66.Wap to print series -1 , 2 ,-3 , 4 ,-5 ……………n

print('''66.Wap to print series -1 , 2 ,-3 , 4 ,-5 ……………n
''')

n=int(input('Enter n: '))

for i in range(1,n+1):
    if i%2==0:
        print(i,end=' , ')
    else:
        print(-i,end=' , ')
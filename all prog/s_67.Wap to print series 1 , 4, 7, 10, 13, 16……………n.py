#program by SUNIL SIR
#67.Wap to print series 1 , 4, 7, 10, 13, 16……………n

print('''67.Wap to print series 1 , 4, 7, 10, 13, 16……………n
''')

n=int(input('Enter n: '))
s=1

for i in range(1,n+1):
    print(s,end=',')
    s=s+3
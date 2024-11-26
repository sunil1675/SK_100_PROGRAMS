#program by SUNIL SIR
#68.Wap to print series 1 , 2, 4, 7, 11, 16 ……………n

print('''68.Wap to print series 1 , 2, 4, 7, 11, 16 ……………n
''')

n=int(input('Enter n: '))
s=1

for i in range(1,n+1):
    print(s,end=',')
    s=s+i
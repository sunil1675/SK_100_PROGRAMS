#program by SUNIL SIR
#63.Wap to print series 1, 8, 27, 64, 125……………n

print('63.Wap to print series 1, 8, 27, 64, 125……………n.\n')

n=int(input('Enter n: '))

for i in range(1,n+1):
    print(i**3,end=',')
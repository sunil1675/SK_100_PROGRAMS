#program by SUNIL SIR
#62.Wap to print series 1, 4, 9, 16, 25,……………n

print('62.Wap to print series 1, 4, 9, 16, 25,……………n.\n')

n=int(input('Enter n: '))

for i in range(1,n+1):
    print(i*i,end=',')
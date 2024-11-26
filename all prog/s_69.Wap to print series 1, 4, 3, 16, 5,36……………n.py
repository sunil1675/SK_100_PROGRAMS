#program by SUNIL SIR
#69.Wap to print series 1, 4, 3, 16, 5,36……………n

print('69.Wap to print series 1, 4, 3, 16, 5,36……………n.\n')

n=int(input('Enter n: '))

for i in range(1,n+1):
    if i%2==0:
        print(i*i,end=',')
    else:
        print(i,end=',')
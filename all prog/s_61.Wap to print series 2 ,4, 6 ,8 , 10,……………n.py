#program by SUNIL SIR
#61.Wap to print series 2 ,4, 6 ,8 , 10,……………n

print('61.Wap to print series 2 ,4, 6 ,8 , 10,……………n.\n')

n=int(input('Enter n: '))

for i in range(1,n+1):
    if i%2==0:
        print(i,end=',')
    else:
        pass
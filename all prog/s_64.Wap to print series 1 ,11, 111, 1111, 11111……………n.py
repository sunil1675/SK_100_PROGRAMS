#program by SUNIL SIR
#64.Wap to print series 1 ,11, 111, 1111, 11111……………n

print('64.Wap to print series 1 ,11, 111, 1111, 11111……………n.\n')

n=int(input('Enter n: '))
s=1

for i in range(1,n+1):
    s=s*10+1
    print(s,end=',')
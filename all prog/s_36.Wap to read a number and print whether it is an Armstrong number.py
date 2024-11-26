#profram by SUNIL SIR
#36.Wap to read a number and print whether it is an Armstrong number.

print('36.Wap to read a number and print whether it is an Armstrong number.\n')

n=int(input('Enter a number: '))
save=n
t=0
s=str(n)
l=len(s)
while n:
    r=n%10
    n=n//10
    t+=(r**l)
if save==t:
    print(f'The total={t},\nSo,yes {save} is an ARMSTRONG NUMBER')
else:
    print(f'The total={t},\nSo,no {save} is not an ARMSTRONG NUMBER')

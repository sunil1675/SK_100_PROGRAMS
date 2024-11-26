#program by SUNIL SIR
#54.Wap to find the LCM and HCF of two numbers.

a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
print()
for i in range(1,(a*b)+1):
    if i%a==0 and i%b==0:
        print('LCM=',i)
        break
    
HCF=0
for i in range(1,(a*b)+1):
    if a%i==0 and b%i==0:
        HCF=i
print('HCF=',HCF)
        
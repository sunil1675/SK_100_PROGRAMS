#Program by SUNIL SIR
#35.Wap to read a number and print sum of each digit

print('''35.Wap to read a number and print sum of each digit
 ''')
n=int(input('Enter a number.- '))
tot=0
while n:                    # let n=1234        #now, n=123
    r=n%10                  # r=4               #r=3
    tot=tot+r               #tot=4              # tot=4+3=7
    n=n//10                 # n=123             # n=12
print(tot)


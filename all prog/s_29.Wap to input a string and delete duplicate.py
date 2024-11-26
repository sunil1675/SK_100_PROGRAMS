#Program by SUNIL SIR
# 29.Wap to input a string and delete duplicate.

print('29.Wap to input a string and delete duplicate.\n')

s=input('Enter string: ')
b=''
for i in s:
    if i not in b:
        b+=i
print(b)
#Program by SUNIL SIR
#28.Wap to input a string and convert lowercase to uppercase and upper to lower.

print('28.Wap to input a string and convert lowercase to uppercase and upper to lower.\n')

s=input('Enter a string: ')
import string

a=''
for i in range (len(s)):
    if s[i] in string.ascii_uppercase:
        a=a+s[i].lower()
    elif s[i] in string.ascii_lowercase:
        a=a+s[i].upper()
    else:
        a=a+s[i]
print()
print(a)
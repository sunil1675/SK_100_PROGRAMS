'''#program by SUNIL SIR
#72.Wap to enter first name middle name and last name and print initial
(Sunil Kumar Sharma = S. K. Sharma)'''

print('''72.Wap to enter first name middle name and last name and print initial
(Sunil Kumar Sharma = S. K. Sharma)''')

f=input("Enter first name: ")
m=input("Enter middle name: ")
l=input("Enter last name: ")

i=f"{f[0].upper()}.{m[0].upper()}.{l.capitalize()}"

print(f"\nFormatted Initials: {i}")
#PROGRM BY SUNIL SIR
#DATED 24-4-24
#21.Wap to print ASCII code for a given digit/character.

print('''21.Wap to print ASCII code for a given digit/character.\n''')

c=input('Enter a character: ')

if len(c)==1:
    a=ord(c)
    print(f'\nThe ASCII code for {c} is {a}')
    
else:
    print(f'\nEnter single chracter')
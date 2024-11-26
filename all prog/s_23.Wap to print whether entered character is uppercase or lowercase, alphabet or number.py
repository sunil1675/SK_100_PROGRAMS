#PROGRAM BY SUNIL SIR
#23.Wap to print whether entered character is uppercase or lowercase, alphabet or number.

import string

print("23. WAP to check if the entered character is uppercase, lowercase, alphabet, or number.\n")

c = input('Enter a character: ')

if len(c) == 1:
    if c in string.ascii_uppercase:
        print(f'The character {c} is a alphabet in uppercase .')
        
    elif c in string.ascii_lowercase:
        print(f'The character {c} is a alphabet in lowercase.')
        
    elif c in string.digits:
        print(f'The character {c} is a number.')
        
    else:
        print(f'The character {c} is neither an alphabet nor a number.')
else:
    print('Please enter a single character.')
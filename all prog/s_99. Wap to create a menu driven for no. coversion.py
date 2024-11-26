#program by SUNIL SIR
'''#99. Wap to create a menu driven interface for all type of binary, decimal, octal, hexadecimal
number conversion'''

print('''99. Wap to create a menu driven interface for all type of binary, decimal, octal, hexadecimal
number conversion''')

while True:
    print('1.Converting Decimal ')
    print('2.Converting Binary')
    print('3.Converting Octal')
    print('4.Converting Hexadecimal')
    print('0.Exit')
    print('======================================')

    ch=int(input(' Enter your choice'))
    print()
    
    if ch==1:
        d=int(input("Enter a decimal number: "))
        print("Binary:", bin(d)[2:])
        print("Octal:", oct(d)[2:])
        print("Hexadecimal:", hex(d)[2:])
    
    elif ch==2:
        b=input("Enter a binary number: ")
        deci=int(b,2)
        print("Decimal:", int(b,2))
        print("Octal:", oct(deci)[2:])
        print("Hexadecimal:", hex(deci)[2:])
    
    elif ch==3:
        o=input("Enter a octal number: ")
        deci=int(o,8)
        print("Decimal:", deci)
        print("Binary:", bin(deci)[2:])
        print("Hexadecimal:", hex(deci)[2:])
    
    elif ch==4:
        h=input("Enter a hexadecimal number: ")
        deci=int(h,16)
        print("Decimal:", deci)
        print("Binary:", bin(deci)[2:])
        print("Octal:", oct(deci)[2:])

    elif ch==0:
        print('\n Ending the program....')
        quit()

    else:
        print('\n Not a choice.')
        print('Try again')

    input('\n Press ENTER to continue')
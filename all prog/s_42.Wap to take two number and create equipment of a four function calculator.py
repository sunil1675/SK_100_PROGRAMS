#program by SUNIL SIR
#42.Wap to take two number and create equipment of a four function (+, -, *, /) calculator

while True:
    print('\n42.Wap to take two number and create equipment of a four function (+, -, *, /) calculator')
    print('======================================')
    print('1.Add 2 no.')
    print('2.Subtract 2 no.')
    print('3.Multiply 2 no.')
    print('4.Divide 2 no.')
    print('0.Exit')
    print('======================================')

    ch=int(input(' Enter your choice '))
    print()
    if ch==1:
        print('Addition of 2 numbers\n')
        a=int(input('Enter a number: '))
        b=int(input('Enter a number: '))
        c=a+b
        print(f'Sum of {a} & {b} = {c}')

    elif ch==2:
        print('Subtraction of 2 numbers\n')
        a=int(input('Enter a number: '))
        b=int(input('Enter a number: '))
        c=a-b
        print(f'Difference of {a} & {b} = {c}')
        
    elif ch==3:
        print('Multiplication of 2 numbers\n')
        a=int(input('Enter a number: '))
        b=int(input('Enter a number: '))
        c=a*b
        print(f'Product of {a} & {b} = {c}')

    elif ch==4:
        print('Division of 2 numbers\n')
        a=int(input('Enter a number: '))
        b=int(input('Enter a number: '))
        c=a/b
        print(f'Division of {a} & {b} = {c}')
            
    elif ch==0:
        print('\n Ending the program....')
        quit()

    else:
        print('Not a choice.')
        print('Try again')

    input('\n Press ENTER to continue')
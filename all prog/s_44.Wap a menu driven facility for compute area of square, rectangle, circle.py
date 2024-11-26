"""Program by SUNIL SIR
44.Wap a menu driven facility for compute area of square, rectangle, circle.
"""

print('''44.Wap a menu driven facility for compute area of square, rectangle, circle.
''')

while True:
    print('\n M E N U    D R I V E N    P R O G R A M')
    print('==============================================')
    print('1.Area of Rectangle')
    print('2.Area of Square')
    print('3.Area of Circle')
    print('0.Exit')
    print('===============================================')

    ch=int(input(' Enter your choice: '))

    if ch==1:
        print("\nPROGRAM TO GET AREA OF RECTANGLE")
        h=int(input('\nEnter Height-> '))
        b=int(input('Enter Breadth-> '))
        ar=1/2*b*h
        print(f'AREA= {ar}cm^2')

    elif ch==2:
        print("\nPROGRAM TO GET AREA OF SQUARE")
        s=int(input('\nEnter Side-> '))
        ar=s*s
        print(f'AREA= {ar}cm^2')

    elif ch==3:
        print("\nPROGRAM TO GET AREA OF CIRCLE")
        r=int(input('\nEnter Radius-> '))
        ar=3.14*r*r
        print(f'AREA= {ar}cm^2')

    elif ch==0:
        print('\n Ending the program....')
        quit()

    else:
        print('\n Not a choice.')
        print('Try again')

    input('\nPress ENTER to continue')


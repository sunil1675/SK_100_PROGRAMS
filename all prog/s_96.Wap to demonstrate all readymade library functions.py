#program by SUNIL SIR
#96.Wap to demonstrate all readymade library functions

print('96.Wap to demonstrate all readymade library functions')

while True:
    print('\n\n\n M E N U    D R I V E N    P R O G R A M')
    print('======================================')
    print('1.abs()')
    print('2.bin()')
    print('3.oct()')
    print('4.hex()')
    print('5.chr()')
    print('6.ord()')
    print('7.bool()')
    print('8.int()')
    print('9.list()')
    print('10.str()')
    print('11.tuple()')
    print('12.dict()')
    print('13.set()')
    print('14.type()')
    print('15.id()')
    print('16.help()')
    print('17.dir()')
    print('18.divmod()')
    print('19.eval()')
    print('20.float()')
    print('21.format()')
    print('22.input()')
    print('23.print()')
    print('24.len()')
    print('25.min()/max()')
    print('26.pow()')
    print('27.round()')
    print('28.sum()')
    print('29.sorted()')
    print('30.reversed()')
    print('31.range()')
    print('0.Exit')
    print('======================================')

    ch=int(input(' Enter your choice'))

    if ch==1:
        print('\nabs()')
        n=int(input('Enter an integer to get the absolute value: '))
        a=abs(n)
        print(f'\nAbsolute value of the number is {a}')
    
    elif ch==2:
        print('\nbin()')
        n=int(input('Enter an integer to convert into binary number: '))
        b=bin(n)
        print(f'\nBinary of the number is {b}')
    elif ch==3:
        print('\noct()')
        n=int(input('Enter an integer to convert into octal number : '))
        o=oct(n)
        print(f'\nOctal of the number is {o}')
    elif ch==4:
        print('\nhex()')
        n=int(input('Enter an integer to convert into hexadecimal number : '))
        h=hex(n)
        print(f'\nHexadecimal of the number is {h}')
    elif ch==5:
        print('\nchr()')
        n=int(input('Enter an the number to get the specified character : '))
        c=chr(n)
        print(f'\n{n} is the unicode no. for: {c}')
    elif ch==6:
        print('\nord()')
        c=input('Enter a character to ger the unicode  : ')
        o=ord(c)
        print(f'\nUnicode of {c}: {o}')
    elif ch==7:
        print('\nbool()')
        n=int(input('Enter an integer to get the boolean value: '))
        b=bool(n)
        print(f'\nBoolean value of the number is {b}')
    elif ch==8:
        print('\nint()')
        n=input('Enter an number to get it in integer: ')
        i=int(n)
        print(f'\nInteger value of the string is {i}')
    elif ch==9:
        print('\nlist()')
        n=(1,2,3,4,5,6,7)
        l=list(n)
        print(f'\nConverting {n} into list: {l}')
    elif ch==10:
        print('\nstr()')
        n=int(input('Enter an integer to get it in string form: '))
        s=str(n)
        print(f'\nString form of the number is {s}')
    elif ch==11:
        print('\ntuple()')
        n=[1,2,3,4,5,6,7,8,9]
        t=tuple(n)
        print(f'\nConverting {n} into tuple: {t}')
    elif ch==12:
        print('\ndict()')
        n=input('Enter name: ')
        a=int(input('Enter age:'))
        c=input('Enter country: ')
        d=dict(name=n, age=a, country=c)
        print(f'\nConverting into dictionary: {d}')
    elif ch==13:
        print('\nset()')
        n=[1,2,3,4,4,4,4,4]
        s=set(n)
        print(f'\nConverting {n} into set: {s}')
    elif ch==14:
        print('\ntype()')
        n=type(5)
        t=type('Hii')
        print(f'''\nType of 5:{n}\nType of 'Hii': {t}''')
    elif ch==15:
        print('\nid()')
        c=input('Enter a character to get the id : ')
        i=id(c)
        print(f'\id of {c}: {i}')
    elif ch==16:
        print('\nhelp()')
        help()
    elif ch==17:
        print('\ndir()')
        dir()
    elif ch==18:
        print('\ndivmod()')
        n1=int(input('Enter a no.: '))
        n2=int(input('Enter a no.: '))
        d=divmod(n1,n2)
        print(f'\nQuotient and Remainder are: {d}')
    elif ch==19:
        print('\neval()')
        n=input('Enter an equation: ')
        a=eval(n)
        print(f'\nSolution of the equation is {a}')
    elif ch==20:
        print('\nfloat()')
        n=input('Enter an number to get it in float: ')
        f=float(n)
        print(f'\nFloat value of the string is {f}')
    elif ch==21:
        print('\nformat()')
        n=input('Enter name: ')
        a=int(input('Enter age:'))
        d="My name is {} and I am {} years old.".format(name, age)
        print(d)
    elif ch==22:
        print('\ninput()')
        i=input('Enter anything to input: ')
    elif ch==23:
        print('\nprint()')
        p=input('Enter anything to print: ')
        print(f'Printing the thing you inputed:\n{p}')
    elif ch==24:
        print('\nlen()')
        i=input('Enter anything to get the length: ')
        l=len(i)
        print(f'Length of {i} is: {l}')
    elif ch==25:
        print('\nmin()/max()')
        n=(1,2,3,4,5,6,7)
        mi=min(n)
        ma=max(n)
        print(f'\nIn the List {n} Maximum no is {ma} and Minimum is {mi}')
    elif ch==26:
        print('\npow()')
        n=int(input('Enter a no.: '))
        p=int(input('Enter the power: '))
        d=pow(n,p)
        print(f'\n{n} to the power of {p} is: {d}')
    elif ch==27:
        print('\nround()')
        n=float(input('Enter a float to get the round off: '))
        r=round(n)
        print(f'\nRound off valu of {n} is {r}')
    elif ch==28:
        print('\nsum()')
        n=[1,2,3,4,5,6,7]
        s=sum(n)
        print(f'\nSum of list {n} is {s}')
    elif ch==29:
        print('\nsorted()')
        n=[12,32,23,24,15,76,7]
        s=sorted(n)
        print(f'\nAscending of list {n} is: {s}')
    elif ch==30:
        print('\nreversed()')
        n=[12,32,23,24,15,76,7]
        s=sorted(n,reverse=True)
        print(f'\nDecending of list {n} is: {s}')
    elif ch==31:
        print('\nrange()')
        s=int(input('Enter start point: '))
        e=int(input('Enter end point: '))
        l=[*range(s,e)]
        print(f'\nList= {l}')
    elif ch==0:
        quit()
    else:
        print('CHOOSE THE ABOVE OPTION ONLY!!')
    input('\n\nPRESS ENTER TO CONTINUE\n\n')
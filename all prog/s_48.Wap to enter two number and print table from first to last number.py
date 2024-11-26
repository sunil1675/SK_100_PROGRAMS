#program by SUNIL SIR
#48.Wap to enter two number and print table from first to last number.

print('''48.Wap to enter two number and print table from first to last number.
''')

s=int(input('Enter the value of starting point: '))
e=int(input('Enter the value of ending point: '))

for n in range(s,e+1):
    print(f"\nMultiplication Table for {n}\n")
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")
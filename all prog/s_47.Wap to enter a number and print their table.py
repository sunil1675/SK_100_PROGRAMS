#program by SUNIL SIR
#47.Wap to enter a number and print their table

print('47.Wap to enter a number and print their table.\n')

n=int(input('Enter the value of n: '))

print(f"\nMultiplication Table for {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
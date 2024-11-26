#program by SUNIL SIR
#70.Wap to create for loop to print different format(with numbers)

print('70.Wap to create for loop to print different format (with numbers).\n')

n=int(input('Enter no.: '))

''' I
        1
        12
        123
        1234
        12345 '''

for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j ,end='')

print()

''' II
        1
        22
        333
        4444
        55555 '''

for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(i,end='')

print()
print()

''' III
        5
        45
        345
        2345
        12345 '''

for i in range(n,0,-1):
    
    for k in range(i-1):
        print('',end='')
    for j in range(i,n+1):
        print(j ,end='')
    print()
 
print()

''' IV
        55555
        4444
        333
        22
        1
 '''

for i in range(n,0,-1):
    print()
    for j in range(1,i+1):
        print(i,end='')

print()
print()

''' V
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5 '''

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
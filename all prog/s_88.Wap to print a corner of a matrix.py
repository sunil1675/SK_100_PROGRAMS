#program by SUNIL SIR
#88.Wap to print a corner of a matrix.

print('88.Wap to print a corner of a matrix')

r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
import random
a=[random.randint(1,100) for i in range(r*c)]
m=[]

co=0
print('\nMatrix: ')
for i in range(r):
    t=[]
    for j in range(c):
        t.append(a[co])
        co+=1
    m.append(t)
for i in range(r):
    print()
    for j in range(c):
        print(m[i][j], end="\t")

print(f'\n\nCorners of matrix: ')
for i in range(r):
    print()
    for j in range(c):
        if (i==0 and j==0) or (i==0 and j==c-1) or (i==r-1 and j==0) or (i==r-1 and j==c-1):
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")


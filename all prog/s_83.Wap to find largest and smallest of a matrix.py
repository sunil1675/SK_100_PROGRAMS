#program by SUNIL SIR
#83.Wap to find largest and smallest of a matrix.

print('83.Wap to find largest and smallest of a matrix.')

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

print('\n\nSmallest of the matrix: ',min(a))
print('Largest of the matrix: ',max(a))
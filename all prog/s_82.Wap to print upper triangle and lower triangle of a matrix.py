#program by SUNIL SIR
#82.Wap to print upper triangle and lower triangle of a matrix

print('82.Wap to print upper triangle and lower triangle of a matrix')

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

print("\n\nUpper triangle:")
for i in range(r):
    print()
    for j in range(c):
        if j>=i:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")
print("\n\nLower triangle:")
for i in range(r):
    print()
    for j in range(c):
        if i>=j:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")

#program by SUNIL SIR
#79.Wap to multiply two matrices.

print('79.Wap to multiply two matrices.')

r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
import random
a=[random.randint(1,100) for i in range(r*c)]
b=[random.randint(1,100) for i in range(r*c)]
m1=[]
m2=[]
co=0

print('\nMatrix 1: ')
for i in range(r):
    t=[]
    for j in range(c):
        t.append(a[co])
        co+=1
    m1.append(t)
for i in range(r):
    print()
    for j in range(c):
        print(m1[i][j], end="\t")

co=0
print('\nMatrix 2: ')
for i in range(r):
    t=[]
    for j in range(c):
        t.append(b[co])
        co+=1
    m2.append(t)
for i in range(r):
    print()
    for j in range(c):
        print(m2[i][j], end="\t")

m3=[]
print('\n\nADDTION ')
for i in range(r):
    t=[]
    for j in range(c):
        q=m1[i][j]*m2[i][j]
        t.append(q)
    m3.append(t)
for i in range(r):
    print()
    for j in range(c):
        print(m3[i][j], end='\t')

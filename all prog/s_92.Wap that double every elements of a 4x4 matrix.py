#program by SUNIL SIR
#92.Wap that double every elements of a 4x4 matrix.

print('92.Wap that double every elements of a 4x4 matrix.')

r=4
c=4
import random
a=[random.randint(1,100) for i in range(r*c)]
b=[random.randint(1,100) for i in range(r*c)]
m1=[]
m2=[]
co=0

print('\nMatrix : ')
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
        

m2=[]
print('\n\nDOUBLE: ')
for i in range(r):
    t=[]
    for j in range(c):
        q=m1[i][j]+m1[i][j]
        t.append(q)
    m2.append(t)
for i in range(r):
    print()
    for j in range(c):
        print(m2[i][j], end='\t')
#program by SUNIL SIR
#80.Wap to transpose a matrix.
import random

print('''80.Wap to transpose a matrix.''')

a=[random.randint(1,100) for i in range(9)]
r=3
c=3
m=[]

co=0

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

#Transposing.....
print()

for i in range (r):
    print()
    for j in range (c):
        print(m[j][i], end="\t")
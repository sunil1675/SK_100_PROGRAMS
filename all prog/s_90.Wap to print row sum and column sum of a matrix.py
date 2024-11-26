#program by SUNIL SIR
#90.Wap to print row sum and column sum of a matrix.

print('90.Wap to print row sum and column sum of a matrix.')

r=3
c=3
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
rs=[]
cs=[]
for i in range(3):
    t=0
    p=0
    for j in range(3):
         t=t+m[i][j]
         p=p+m[j][i]
    rs.append(t)
    cs.append(p)
print("\nRow Sum\n",rs)
print("\nColumn Sum\n",cs)
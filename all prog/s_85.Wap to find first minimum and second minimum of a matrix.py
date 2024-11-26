#prgram by SUNIL SIR
#85.Wap to find first minimum and second minimum of a matrix.

print('85.Wap to find first minimum and second minimum of a matrix.')

r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
import random
a=[random.randint(1,100) for i in range(r*c)]
m=[]
co=0

print('\nMatrix : ')
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

if len(a)<2:
    print("\n\nNot enough elements to find both first and second minimumss.")
else:
    u=list(set(a))
    u.sort(reverse=False)
    m1=u[0]
    m2=u[1] if len(u)>1 else "No second maximum"

    print(f'\n\nFirst Minimum: {m1}')
    print(f'Second Minimum: {m2}')

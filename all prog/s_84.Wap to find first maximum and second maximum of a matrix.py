#prgram by SUNIL SIR
#84.Wap to find first maximum and second maximum of a matrix.

print('84.Wap to find first maximum and second maximum of a matrix.')

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
    print("\n\nNot enough elements to find both first and second maximums.")
else:
    u=list(set(a))
    u.sort(reverse=True)
    m1=u[0]
    m2=u[1] if len(u)>1 else "No second maximum"

    print(f'\n\nFirst Maximum: {m1}')
    print(f'Second Maximum: {m2}')
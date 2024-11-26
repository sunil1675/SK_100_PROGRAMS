#program by SUNIL SIR
#91.Wap to print sum the elements above and below main diagonal of a matrix.

print('91.Wap to print sum the elements above and below main diagonal of a matrix.')

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

sa=0
sb=0
for i in range(r):
    for j in range(c):
        if i<j:
            sa=sa+m[i][j]
        elif i>j:
            sb=sb+m[i][j]
            
print("\n\nAbove main Diagonal:")
for i in range(r):
    print()
    for j in range(c):
        if i<j:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")
print(f'\nSum= {sa}\n')
print("\nBelow main Diagonal:")
for i in range(r):
    print()
    for j in range(c):
        if i>j:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")
print(f'\n\nSum= {sb}\n')

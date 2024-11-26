'''#program by SUNIL SIR
#81.Wap to print diagonal elements of a matrix x [p][q]
1. First diagonal a00, a11, a22…ap-1,p-1
2. 1. First diagonal a0q-1, a1q-2, a2 q-3…ap-1,q-p+1
'''

print('''81.Wap to print diagonal elements of a matrix x [p][q]
1. First diagonal a00, a11, a22…ap-1,p-1
2. 1. First diagonal a0q-1, a1q-2, a2 q-3…ap-1,q-p+1
''')

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

print("\n\n1st diagonal (left-to-right):")
for i in range(r):
    print()
    for j in range(c):
        if i==j:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")

print('\n\n2nd diagonal (right-to-left): ')
for i in range(r):
    print()
    for j in range(c):
        if j==c-i-1:
            print(m[i][j], end="\t")
        else:
            print(" " ,end="\t")

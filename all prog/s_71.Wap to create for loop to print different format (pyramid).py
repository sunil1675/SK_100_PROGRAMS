#program by SUNIL SIR
#71.Wap to create for loop to print different format (pyramid)

print('71.Wap to create for loop to print different format (pyramid)\n')

w='ANTHONY'
n=len(w)


print('=*'*30)

''' I
        A n t h o n y '''
for i in range(n):
    print(w[i],end=' ')

print()
print('=*'*30)

''' II
        A
        N
        T
        H
        O
        N
        Y '''
for i in range(n):
    print(w[i])

print()
print('=*'*30)

''' III
        A
        A N
        A N T
        A N T H
        A N T H O
        A N T H O N
        A N T H O N Y '''
for i in range(1,n+1):
    print()
    for j in range(i):
        print(w[j] ,end=' ')

print()
print('=*'*30)

''' IV
        A
        N N
        T T T
        H H H H
        O O O O O
        N N N N N N
        Y Y Y Y Y Y Y
 '''
for i in range(n):
    print()
    for j in range(i+1):
        print(w[i], end=' ')

print()
print('=*'*30)

''' V
          A
         A N
        A N T
       A N T H
      A N T H O
     A N T H O N
    A N T H O N Y '''
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i+1):
        print(w[j], end=" ")
    print()

print()
print('=*'*30)

''' VI
        A N T H O N Y
         A N T H O N
          A N T H O
           A N T H
            A N T
             A N
              A       '''
for i in range(n,0,-1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(w[j], end=" ")
    print()

print()
print('=*'*30)

''' VII
            A
          A B C
         A B C D
        A B C D E
         A B C D
          A B C
           A B
            A           '''

n = 5
for i in range(1,n+1):
    print(" " *(n-i),end="")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()
    
for i in range(n-1,0,-1):
    print(" " *(n-i),end="")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()

print()
print('=*'*30)
n=len(w)

''' VIII
            A
          A N
        A N T
      A N T H
    A N T H O
  A N T H O N
A N T H O N Y '''
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i):
        print(w[j], end=' ')
    print()

print()
print('=*'*30)
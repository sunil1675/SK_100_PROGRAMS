#program by SUNIL SIR
#95. Wap with a function which ask for a password and verify it.

print('95. Wap with a function which ask for a password and verify it.')

p=input('Enter password: ')
status= False
for i in range(0,10):
    for j in range(0,10):
        s=str(i)+str(j)
        if p==s:
            print('\nPassword found:', p)
            status=True
            break
    if status:
        break
else:
    print("Password not found in the two-digit range.")
#program by SUNIL SIR
#87.Wap to convert a matrix into a vector.
print('''87.Wap to convert a matrix into a vector.''')

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ]
print(f'Matrix: {m}')

v=[]
c=0
for i in range(3):
    for j in range(3):
        v.append(m[i][j])
        c+=1
print(v)
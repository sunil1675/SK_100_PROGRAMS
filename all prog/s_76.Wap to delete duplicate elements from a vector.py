#program by SUNIL SIR
#76.Wap to delete duplicate elements from a vector.

print('76.Wap to delete duplicate elements from a vector.')

n=int(input("Enter the number of elements in the vector: "))
v=[]
print()
for i in range(n):
    e=input(f"Enter element{i+1}: ")
    v.append(e)

u=list(set(v))

print(f"\nVector after removing duplicates: {u}")

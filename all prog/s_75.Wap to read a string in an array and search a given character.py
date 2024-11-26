#program by SUNIL SIR
#75.Wap to read a string in an array and search a given character.

print('75.Wap to read a string in an array and search a given character.')

n=int(input('Enter no. of string: '))
l=[]

for i in range(n):
    s=input(f"Enter string{i+1}: ")
    l.append(s)
print()

c=input('Enter character to serch for: ')
for i in range(n):
    if c in l[i]:
        print(f"Character '{c}' found in string {i+1} ({l[i]}).")
    else:
        print(f"Character '{c}' not found in string{i+1} ('{l[i]}').")

#program by SUNIL SIR
#74.Wap to read a string in an array and print their length.

print('''74.Wap to read a string in an array and print their length.
''')

n = int(input("Enter the number of strings: "))
s=[]

for i in range(n):
    w=input(f"Enter string {i + 1}: ")
    s.append(w)

print()

for i in range(n):
    print(f"Length of string {i + 1} ('{s[i]}'): {len(s[i])}")
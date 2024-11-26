#program by SUNIL SIR
#77.Wap to find substring from a main string.

print('''77.Wap to find substring from a main string.
''')

m=input("Enter the main string: ")
s=input("Enter the substring to search for: ")
print()

if s in m:
    p=m.find(s)
    print(f"Substring '{s}' found in the main string at position {p}.")
else:
    print(f"Substring '{s}' not found in the main string.")

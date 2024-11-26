'''#Program by SUNIL SIR
#57.Wap to accept the age of n employee and count the number of person in the following age
group. A. Under 18 B. 18-25 C. 260 50 D 51- 80 E above 80
'''

print('''57.Wap to accept the age of n employee and count the number of person in the following age group.
A. Under 18 B. 18-25 C. 260 50 D 51- 80 E above 80
''')

n = int(input("Enter the number of employees: "))

u_18=0
a_18_25=0
a_26_50=0
a_51_80=0
a_80=0

for i in range(n):
    age=int(input(f"Enter age of employee {i+1}: "))
    
    if age<18:
        u_18+=1
    elif 18<=age<=25:
        a_18_25+=1
    elif 26<=age<=50:
        a_26_50+=1
    elif 51<=age<=80:
        a_51_80+=1
    else:
        a_80+=1

print("\nNumber of persons in each age group:")
print(f"A. Under 18: {u_18}")
print(f"B. 18-25:    {a_18_25}")
print(f"C. 26-50:    {a_26_50}")
print(f"D. 51-80:    {a_51_80}")
print(f"E. Above 80: {a_80}")
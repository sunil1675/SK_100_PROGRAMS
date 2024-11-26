#program by SUNIL SIR
#39.Wap to enter n number and calculate average of that number.

print("39.WAP to enter n numbers and calculate the average of those numbers.\n")

n=int(input('Enter the no. of numbers you wanna get the average of: '))
print()
t=0
for i in range(n):
    e=float(input('Enter a no.:'))
    t=t+e

av=t/n
print(f'Average of {n} numbers is {av}')
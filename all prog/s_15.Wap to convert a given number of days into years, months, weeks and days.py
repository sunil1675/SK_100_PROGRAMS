#Program by SUNIL SIR
#15.Wap to convert a given number of days into years, months, weeks and days.

print("15.Wap to convert a given number of days into years, months, weeks and days\n")

n=int(input("Enter the no. of Days: "))

y= int(n/365)
m=int((n % 365)//30)
w= int(((n % 365)%30)//7) 
d= int((n % 365) % 7)

print(f"{n} days is equivalent to {y} years, {m} months, {w} weeks, and {d} days.")
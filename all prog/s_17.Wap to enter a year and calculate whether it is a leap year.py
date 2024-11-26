#program by SUNIL SIR
#17.Wap to enter a year and calculate whether it is a leap year.

print('17.Wap to enter a year and calculate whether it is a leap year. \n')

y=int(input('Enter year: '))
if y%400==0 or (y%4==0 and y%10!=0):
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")
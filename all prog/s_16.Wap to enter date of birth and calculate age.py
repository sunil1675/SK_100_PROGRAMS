#Program by SUNIL SIR
#16.Wap to enter date of birth and calculate age

from datetime import date, timedelta

print('''16.Wap to enter date of birth and calculate age''')

def age_calculator(birthdate):
   today = date.today()
   age = (today - birthdate) // timedelta(days=365.2425)
   return age

y=int(input('Enter Year: '))
m=int(input('Enter Month: '))
d=int(input('Enter Date: '))

birthdate= date(y,m,d)
age= age_calculator(birthdate)

print(f"\nThe age of the person in years is {age} years")
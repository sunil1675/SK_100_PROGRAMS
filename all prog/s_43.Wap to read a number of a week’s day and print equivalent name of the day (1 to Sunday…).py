'''program by SUNIL SIR
43.Wap to read a number of a week’s day and print equivalent name of the day (1 to Sunday…).
'''

print('''43.Wap to read a number of a week’s day and print equivalent name of the day (1 to Sunday…).
''')

d={1:'Sunday',2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday',6:'Friday',7:'Saturday'}
n=int(input("Enter a number (1-7) to get the day of the week: "))

if n in d:
    print('The day is:',d[n])
else:
    print('Invalid choice')
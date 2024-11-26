'''#program by SUNIL SIR
#73.Wap to accept name and time and print name with welcome wish according to time
(Hello name good morning if time is < 12, good afternoon, evening)'''

print('''73.Wap to accept name and time and print name with welcome wish according to time
(Hello name good morning if time is < 12, good afternoon, evening)\n''')

n=input('Enter your name: ')
t=int(input('Enter the time in 24-hour format (0-23): '))

if 0<=t<12:
    g='Good Morning'
elif 12<=t<17:
    g='Good Afternoon'
elif 17<=t<21:
    g='Good Evening'
else:
    g='Good Night'

print(f'\nHello {n}, {g}!!')
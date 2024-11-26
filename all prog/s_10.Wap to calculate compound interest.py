#PROGRM BY SUNIL SIR
#DATED 24-4-24
#10.Wap to calculate compound interest

print('10.Wap to calculate compound interest  \n')

p=float(input("Enter Principal amount: "))
r=float(input("Enter Annual Rate of Interest (in percentage): ")) / 100
n=int(input("Enter Number of Times Interest Applied per Time Period: "))
t=float(input("Enter Number of Time Periods Elapsed: "))

a=p*(1+r/n)**(n*t)
ci=a-p

print(f'\nCompound Interest= {ci:.2f}')


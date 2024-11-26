#program by SUNIL SIR
#55.Wap to print truth table for xy+z.(for and ,or )

print('55.Wap to print truth table for xy+z.(for and ,or )')

print(' x   y    z     xy    xy+z ')
print('-'*30)

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            xy = x and y
            r=(x and y) or z
            
            print(f"{x}  | {y}  | {z}  |  {xy}  |   {r}   |")

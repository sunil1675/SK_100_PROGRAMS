#program by SUNIL SIR
'''#93. Wap to create a function to draw a box by given parameter (left, top, right, bottom) use ASCII
character to draw corner and lines'''

print('''93. Wap to create a function to draw a box by given parameter (left, top, right, bottom) use ASCII
character to draw corner and lines''')

def box():
    print("╔",end="")
    
    for i in range(w-1):
        print("═",end="")
    print("╗",end="")
    print()

    for i in range(h):
        print("║"+" "*(w-2),"║")

    print("╚",end="")
    for i in range(w-1):
        print("═",end="")
        
    print("╝",end="")

h=int(input('Enter height: '))
w=int(input('Enter width: '))

box()
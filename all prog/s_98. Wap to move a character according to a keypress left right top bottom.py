#program by SUNIL SIR
#98. Wap to move a character according to a keypress left right top bottom.

print('98. Wap to move a character according to a keypress left right top bottom.')

from tkinter import *
w=Tk()
w.geometry('500x400')
xx=200
yy=200

def mu(e):
    global yy
    yy-=20
    b1.place(x=xx, y=yy)
    
def md(e):
    global yy
    yy+=20
    b1.place(x=xx, y=yy)

def ml(e):
    global xx
    xx-=20
    b1.place(x=xx, y=yy)

def mr(e):
    global xx
    xx+=20
    b1.place(x=xx, y=yy)

b1=Button(w,font=(24), text="@")
b1.place(x=xx,y=xx)

w.bind("<Left>", ml)
w.bind("<Right>", mr)
w.bind("<Up>", mu)
w.bind("<Down>", md)

w.mainloop()
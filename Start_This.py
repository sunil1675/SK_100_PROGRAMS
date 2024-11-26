from tkinter import *
from tkinter import ttk
import os

w=Tk()
w.geometry("900x600+200+10")
n = StringVar() 
cb=ttk.Combobox(w, width = 130, textvariable = n) 
cb.place(x=50,y=50)


txt=Text(w,width=100,height=30)
txt.place(x=50,y=80)


def fill():
    os.chdir("all prog\\")
    dnm=os.listdir()
    item=[]
    for i in range(len(dnm)):
        item.append(dnm[i])
        
    cb.configure(values=item)
    
def load(e):
    fnm=cb.get()
    print()
    txt.delete(1.0,END)
    f=open(fnm,encoding='utf-8')
    s=f.read()
    f.close()
    txt.insert(1.0,s)
    

cb.bind("<<ComboboxSelected>>",load)

w.after(1000,fill)
w.mainloop()


    

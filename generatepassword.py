from tkinter import *
import string
import random

def password_generator(size,choice):
    rand = ''.join(random.choices(choice,k=size))
    return rand
    #pw_lbl.config(text=rand)

def processData(sy,nu,lo,up):
    total = ""
    if(sy == 0 and nu == 0 and lo == 0 and up == 0):
        total += string.ascii_letters
    if(sy == 1):
        total += string.punctuation
    if(nu == 1):
        total += string.digits
    if(lo == 1):
        total += string.ascii_lowercase
    if(up == 1):
        total += string.ascii_uppercase
    return total

def answer(leng,syms,nums,lows,upps):
    lengs = int(leng.get())
    symes = int(syms.get())
    numes = int(nums.get())
    lowes = int(low.get())
    uppes = int(upper.get())
    pw = password_generator(lengs,processData(symes,numes,lowes,uppes))
    pw_lbl.config(text=pw)

root = Tk()
root.title("Random Password generator")
root.geometry("450x200")

options = range(1,26)
length = IntVar()
sym = IntVar()
num = IntVar()
low = IntVar()
upper = IntVar()
length.set(options[0]) # starts with the first item

title = Label(root,text="Password Generator",font=("Helvetica",20,"bold", UNDERLINE))
drop_lbl = Label(root,text="Password Length: ")
drop = OptionMenu(root, length, *options,) #use * for a list
symbol_lbl = Label(root,text="Include Symbols: ") # string.punctuation
symbol_btn = Checkbutton(root,variable=sym)
number_lbl = Label(root,text="Include Numbers: ") # string.digits
number_btn = Checkbutton(root,variable=num)
lower_lbl = Label(root,text="Include Lowercase Characters: ") #string.ascii_lowercase
lower_btn = Checkbutton(root,variable=low)
upper_lbl = Label(root,text="Include Uppercase Characters: ") #string.ascii_uppercase
upper_btn = Checkbutton(root,variable=upper)
gernate_btn = Button(root, text="Generate Password",fg="blue",relief=RAISED,command=lambda: answer(length,sym,num,low,upper))
pw_lbl = Label(root)

title.grid(row=0)
drop_lbl.grid(row=1,sticky=W)
drop.grid(row=1,column=1,sticky=W)
symbol_lbl.grid(row=2,sticky=W)
symbol_btn.grid(row=2,column=1,sticky=W)
number_lbl.grid(row=3,sticky=W)
number_btn.grid(row=3,column=1,sticky=W)
lower_lbl.grid(row=4,sticky=W)
lower_btn.grid(row=4,column=1,sticky=W)
upper_lbl.grid(row=5,sticky=W)
upper_btn.grid(row=5,column=1,sticky=W)
gernate_btn.grid(row=6)
pw_lbl.grid(row=6,column=1)

root.mainloop()

from tkinter import *
import tkinter
import os
import sys
from subprocess import call
import pandas as pd
from PIL import ImageTk,Image

def checkinn():
    call(["python", "checkinn.py"])
def guestlist():
    call(["python", "listof.py"])
def checkout():
    call(["python", "chckout.py"])
def info():
    call(["python", "getinfo.py"])

root = Tk()
root.title("Hotel Management".center(200))
root.geometry("720x480")
root.configure(bg= "Lightgray",highlightbackground = "Lightgray")
b = pd.read_csv("file3.csv")
a = ((b["username"]).to_string(index=False))

frame = Frame(root,borderwidth =1,relief = GROOVE,bg = "Lightgray",width = 650,height =450,highlightbackground = "gray",highlightcolor = "black",highlightthickness= 1).place(x=37,y=10)
image1 = Image.open("download.jpg")
image1 = image1.resize((640, 435), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=40, y=15)
title = Label(frame,text = "WELCOME     " +a ,font = ("serif",25,"bold","underline"),fg = "black",bg = "Lightgray").pack(pady = 20)
button1 = Button(frame,text = "1.  CHECK INN",font = ("serif",10,"bold"),bg = "Lightgray",width = 30,height = 3,fg = "black",bd = 2,relief = RAISED,command = checkinn)
button1.pack()
button2 = Button(frame,text = "2.  SHOW GUESTS LIST",font = ("serif",10,"bold"),bg = "Lightgray",width = 30,height = 3,fg = "black",bd = 2,relief = RAISED,command = guestlist)
button2.pack(pady = 10)
button3 = Button(frame,text = "3.  CHECK OUT",font = ("serif",10,"bold"),bg = "Lightgray",width = 30,height = 3,fg = "black",bd = 2,relief = RAISED,command = checkout)
button3.pack(pady = 10)
button4 = Button(frame,text = "4.  INFO OF GUESTS",font = ("serif",10,"bold"),bg = "Lightgray",width = 30,height = 3,fg = "black",bd = 2,relief = RAISED,command = info)
button4.pack(pady = 10)
button5 = Button(frame,text = "5.  EXIT",font = ("serif",10,"bold"),bg = "Lightgray",width = 30,height = 3,fg = "black",bd = 2,relief = RAISED,command = quit)
button5.pack(pady = 1)


root.mainloop()
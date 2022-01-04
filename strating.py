from tkinter import *
import os
import sys
from subprocess import call
import pandas as pd
from PIL import ImageTk,Image


def submit():
    call(["python", "hotelmanage.py"])

root = Tk()
root.title("LOGIN".center(200))
root.geometry("720x480")
root.configure(bg= "gray",highlightbackground = "gray")

def login():
    way = {"username": [var1.get()],
           "password": [var2.get()]}
    df = pd.DataFrame(way)
    df.to_csv('file3.csv', mode='w', index=False)
    submit()



frame = Frame(root,borderwidth =1,relief = GROOVE,bg = "white",width = 700,height =460,highlightbackground = "black",highlightcolor = "black",highlightthickness= 1).place(x=10,y=10)
img = ImageTk.PhotoImage(Image.open("login.jpg"))
panel = Label(frame, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
labe = Label(frame,text = "PLEASE  REGISTER !",fg = 'red',font= ("arial",25,"bold"),bg= "white")
labe.place(x=190,y=40)
var1 = StringVar()
var2 = StringVar()
label = Label(frame,text = "Username :", fg = "black", font= ("arial",20,"bold","underline"))
label.place(x=100,y=180)
entry = Entry(frame,textvariable = var1,fg = "black", font=("arial",20),width = 20,bd=2)
entry.place(x=300,y=185)
label2 = Label(frame,text = "Password :", fg = "black", font= ("arial",20,"bold","underline"))
label2.place(x=100,y=250),
entry1 = Entry(frame,textvariable = var2,show = "*",fg = "black", font=("arial",20),width = 20,bd=2)
entry1.place(x=300,y=255)

button = Button(frame,text = "REGISTER",fg ="blue",bg="Light blue",width =9,height=2,font= ("arial",20,"bold"),command = login)
button.place(x=280,y=350)
root.mainloop()
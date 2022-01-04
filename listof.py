import os
from tkinter import *
import pandas as pd

class list:
    def __init__(self):
        root = Tk()
        root.title("LIST".center(250))
        root.geometry("850x600")
        root.configure(bg="white", highlightbackground="Lightgray")

        self.frame = LabelFrame(root,text = "LIST OF ALL GUESTS",fg= "black",bg= "white",font = ("arial",18,"bold"),relief = GROOVE,)
        self.frame.place(relx=0.02, rely=0.04, relheight=0.92,relwidth=0.96)
        self.frame1 = Frame(root,bg= "light gray", bd=1,relief = FLAT,highlightbackground="black", highlightthickness=1, width=380, height=440)
        self.frame1.place(x=50,y=80)
        self.frame2 = Frame(root, bg="light gray", bd=1, relief=FLAT, highlightbackground="black",highlightthickness=1, width=330, height=440)
        self.frame2.place(x=460, y=80)
        label1 = Label(self.frame1 , text = "NAMES",fg = "black",bg ="Light gray",font = ("arial",18,"bold"))
        label1.place(x=130,y=10)
        label2 = Label(self.frame2,text = "ROOM NO.",fg = "black", bg = "Light gray",font = ("arial",18,"bold"))
        label2.place(x=100, y=10)
        self.text1 = Text(root, bg="white", bd=1, highlightbackground="black",highlightthickness=1, width=30, height=12,font=("algerian",15,"bold"),wrap = WORD,spacing1=5)
        self.text1.place(x=70, y=140)
        self.text2 = Text(root, bg="white", bd=1, highlightbackground="black", highlightthickness=1,width=26, height=12,font=("algerian",15,"bold"),wrap =WORD,spacing1=5)
        self.text2.place(x=480, y=140)

        op = pd.read_csv("file2.csv")
        s = ((op['name']).to_string(index=True))
        self.text1.insert(INSERT,s )
        p = ((op['room']).to_string(index=False))
        self.text2.insert(INSERT, p + "\n")

        root.mainloop()
list()
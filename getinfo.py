import pandas as pd
import csv
from tkinter import *
from subprocess import call

class info:
    def __init__(self):
        def info():
            self.numb = self.no.get()
            ok = int(self.numb)
            op = pd.read_csv("file2.csv")
            op.set_index("room", inplace=True)
            df = pd.read_csv("file2.csv")
            s = ((op.loc[ok]).to_string(index=True))
            if ok in df.values:
                self.text.insert(INSERT, "" + s +"  ""\n")
            else:
                self.text.insert(INSERT, "NO GUEST FOUND""\n")

            #print(op.loc[ok])



        root = Tk()
        root.title("CHECKOUT".center(300))
        root.geometry("1080x720")
        root.configure(bg="light grey", highlightbackground="Lightgray")

        self.no = StringVar()
        self.frame1 = Frame(root, highlightbackground="black", highlightthickness=1, width=950, height=650, bd=1,
                            relief=GROOVE)
        self.frame1.pack(pady=40)
        label = Label(self.frame1,text= "!!GET INFO OF GUESTS!!",fg= "red",bg= "white", font=("arial", 20, "bold"))
        label.place(x=340,y=40)
        labelling = Label(self.frame1, text="ENTER YOUR ROOM NO.\t:", fg='black', font=("arial", 20, "bold"))
        labelling.place(x=230, y=120)
        entry = Entry(self.frame1, textvariable=self.no, fg="black", font=("arial", 20, "bold"), width=5, bd=2)
        entry.place(x=650, y=120)
        button = Button(self.frame1, relief=RAISED, width=15, height=2, text="CHECK OUT", font=("arial", 20, "bold"),
                        bd=2,command = info)
        button.place(x=320, y=200)
        self.text = Text(self.frame1, bg="light cyan", fg="black", bd=1, height=12, width=75,
                         highlightbackground="black", relief=SUNKEN,
                         highlightthickness=1, font=("arial", 15), wrap=WORD)
        self.text.place(x=55, y=320)
        root.mainloop()
info()
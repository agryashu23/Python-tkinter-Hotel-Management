import pandas as pd
import csv
from tkinter import *
from subprocess import call
from PIL import ImageTk,Image
import tkinter
class checkout:
    def __init__(self):

        def checkut():
            self.room = self.no.get()
            c =int(self.room)
            #print(b)
            df = pd.read_csv("file2.csv")
            #print(df)
            b = df.loc[df['room'] == c]
            #print(b)
            marks_list = b['name'].squeeze()
            #print(marks_list)
            if c >= 50:
                self.text.insert(INSERT, "PLEASE INPUT A VALID ROOM NO.""\n")
            else :
                self.text.insert(INSERT, "VALID ROOM NO.""\n")
            if c not in df.values:
                self.text.insert(INSERT, "NO GUEST FOUND""\n")
            else:
                self.text.insert(INSERT, "THANK YOU!!     " + marks_list + "    FOR VISTING US.""\n")
            op = pd.read_csv("file2.csv", index_col=0)
            op.drop(marks_list, inplace=True)
            op.to_csv('file2.csv', mode='w')


        root = Tk()
        root.title("CHECKOUT".center(300))
        root.geometry("1080x720")
        root.configure(bg="light blue", highlightbackground="Lightgray")

        self.no = StringVar()
        self.frame1 = Frame(root, highlightbackground="black", highlightthickness=1, width=950, height=650, bd= 1,relief =GROOVE)
        self.frame1.pack(pady=40)
        img = ImageTk.PhotoImage(Image.open("bye.jpg").resize((940, 330), Image.ANTIALIAS))
        lbl = tkinter.Label(self.frame1, image=img)
          # Keep a reference in case this code put is in a function.
        lbl.place(x=0,y=0)


        label2 = Label(root, text="Welcome")
        label2.pack(pady=50)
        labelling = Label(self.frame1,text = "ENTER YOUR ROOM NO.\t:",fg= 'black',font= ("arial",20,"bold"))
        labelling.place(x=230,y=60)
        entry = Entry(self.frame1,textvariable = self.no,fg = "black", font= ("arial",20,"bold"),width =5,bd =2)
        entry.place(x=650,y=60)
        button = Button(self.frame1,relief= RAISED, width =15,height=2,text = "CHECK OUT", font= ("arial",20,"bold"),bd=2,command = checkut)
        button.place(x=320,y=220)
        self.text = Text(self.frame1,bg= "light cyan",fg = "black",bd=1,height= 12,width=75,highlightbackground="black",relief= SUNKEN,
                         highlightthickness=1,font= ("arial",15), wrap = WORD)
        self.text.place(x=50,y=330)










        root.mainloop()


checkout()

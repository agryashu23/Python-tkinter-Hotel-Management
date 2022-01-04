from tkinter import *
import pandas as pd
from subprocess import call
import pickle
import csv
Delux = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
Semi_Delux = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
General = (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45)
Joint_Room = (46, 47, 48, 49, 50, 46, 47, 48, 49, 50)



class Hotel:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.number = 0
        self.days =0
        self.price = 0
        self.room = 0

        def file_save(self):
            way = {
                "name": [self.name.get()],
                "address": [self.address.get()],
                "mobile": [self.number.get()],
                "room": [self.room],
                "price": [self.price]
            }
            df = pd.DataFrame(way)
            #print(df)
            listq = [self.name.get(),self.address.get(),self.number.get(),str(self.room),str(self.price)]
            df.to_csv('file2.csv', mode='a',index=False, header=False)
            fo = open("recipt.txt", "w+")
            for h in range(0, 5):
                fo.write(listq[h] + "\n")
            fo.close()
            call(["python", "recei.py"])






        def caps(event):
            self.name.set(self.name.get().upper())
        def tor(self):
            if self.ch ==1:
                self.price = self.price + (2000 *self.days.get())
                self.m= 1
            elif self.ch == 2:
                self.price = self.price + (1500 * self.days.get())
                self.m = 2
            elif self.ch == 3: 
                self.price = self.price + (1000 * self.days.get())
                self.m = 3
            elif self.ch == 4:
                self.price = self.price + (1700 * self.days.get())
                self.m = 4
        def payment_option(self):
            op = self.p
            if op == 2:
                self.price = self.price - ((self.price * 10) / 100)

        def bill(self):

            if self.m == 1:
                a = Delux
            elif self.m == 2:
                a = Semi_Delux
            elif self.m == 3:
                a = General
            elif self.m == 4:
                a = Joint_Room
            col_list = ["name", "address", "mobile", "room", "price"]
            ok = pd.read_csv("file2.csv", usecols=col_list)
            c = ok["room"]
            u = c.values.tolist()
            #print(u)

            for r in a:
                if r not in u:
                    self.room =r
                    #print(r)
                    break
                else:
                    continue
            self.room =r


            file_save(self)

        def submit():
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and  self.var4.get()==0 and  self.var5.get()==1 and  self.var6.get()==0:
                self.ch=1
                self.p=1
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and  self.var4.get()==0 and  self.var5.get()==0 and  self.var6.get()==1:
                self.ch = 1
                self.p = 2
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==0 and self.var2.get()==1 and self.var3.get()==0 and  self.var4.get()==0 and  self.var5.get()==1 and  self.var6.get()==0:
                self.ch = 2
                self.p = 1
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==0 and self.var2.get()==1 and self.var3.get()==0 and  self.var4.get()==0 and  self.var5.get()==0 and  self.var6.get()==1:
                self.ch = 2
                self.p = 2
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==1 and  self.var4.get()==0 and  self.var5.get()==1 and  self.var6.get()==0:
                self.ch = 3
                self.p = 1
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==0 and self.var2.get()==0 and self.var3.get()==1 and  self.var4.get()==0 and  self.var5.get()==0 and  self.var6.get()==1:
                self.ch = 3
                self.p = 2
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==0 and self.var2.get()==0 and self.var3.get()==0 and  self.var4.get()==1 and  self.var5.get()==1 and  self.var6.get()==0:
                self.ch = 4
                self.p = 1
                tor(self)
                payment_option(self)
                bill(self)
            if self.var1.get()==1 and self.var2.get()==0 and self.var3.get()==0 and  self.var4.get()==1 and  self.var5.get()==0 and  self.var6.get()==1:
                self.ch = 4
                self.p = 2
                tor(self)
                payment_option(self)
                bill(self)

        root = Tk()
        root.title("Hotel Management".center(300))
        root.geometry("1080x720")
        root.configure(bg="white", highlightbackground="Lightgray")

        self.frame1 = Frame(root,borderwidth =3,bg = "Lightgray",width = 1000,height =100,highlightbackground = "black",highlightcolor = "black",highlightthickness= 1)
        self.frame1.place(relx=0.03, rely=0.05, relheight=0.12, relwidth=0.93)
        self.label = Label(self.frame1,text ="YOU CLICKED ON     :     CHECK INN",font=("serif",35,"bold"),bg = "Lightgray",fg = "black").pack(pady=20)
        self.frame2 = LabelFrame(root,bd=1,highlightbackground = "black",highlightcolor = "black",highlightthickness= 1)
        self.frame2.place(relx=0.03, rely=0.23, relheight=0.66, relwidth=0.93)
        self.name = StringVar()
        self.days = IntVar()
        self.address = StringVar()
        self.number = StringVar()
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()

        self.a = Label(self.frame2,text = "     ENTER YOUR NAME             :",font=("serif",15,"bold")).grid(row=0,column=0,pady=10,padx=20)
        self.a1 = Entry(self.frame2,textvariable = self.name,fg = "black",font=("serif",15),width = 50,bd=2)
        self.a1.grid(row=0,column=1,padx=60)
        self.a1.bind("<KeyRelease>", caps)
        self.b = Label(self.frame2,text = "    ENTER YOUR ADDRESS       :",font=("serif",15,"bold")).grid(row=1,column=0,padx =20)
        self.b1 = Entry(self.frame2,textvariable = self.address,fg = "black",font=("serif",15),width = 50,bd=2)
        self.b1.grid(row=1,column=1,padx=40,pady=10)
        self.b1.bind("<KeyRelease>", caps)
        self.c = Label(self.frame2,text = "     ENTER YOUR NUMBER        :",font=("serif",15,"bold")).grid(row=2,column=0,pady=10,padx=20)
        self.c1 = Entry(self.frame2,textvariable = self.number,fg = "black",font=("serif",15),width = 50,bd=2)
        self.c1.grid(row=2,column=1,padx=60)
        self.d = Label(self.frame2,text = "    NUMBER OF DAYS               :",font=("serif",15,"bold")).grid(row=3,column=0,pady=10,padx=20)
        self.d1 = Entry(self.frame2,textvariable = self.days,fg = "black",font=("serif",15),width = 50,bd=2)
        self.d1.grid(row=3,column=1,padx=60)
        self.tit = Label(self.frame2,text = "CHOOSE YOUR ROOM ",font=("serif",15,"bold")).place(x=330,y= 200)
        self.chcbutn1 = Checkbutton(self.frame2,text = "DELUXE",width =20,height=2, font = ("serif",15,"bold"),variable =self.var1).grid(row=4,pady=10)
        self.chcbutn2 = Checkbutton(self.frame2,text = "FULL DELUXE",width =20,height=2, font = ("serif",15,"bold"),variable =self.var2).grid(row=5)
        self.chcbutn3 = Checkbutton(self.frame2,text = "GENERAL",width =20,height=2, font = ("serif",15,"bold"),variable =self.var3).grid(row=4,column=1,padx=20,pady=10)
        self.chcbutn4 = Checkbutton(self.frame2,text = "JOINT",width =20,height=2, font = ("serif",15,"bold"),variable =self.var4).grid(row=5,column=1)
        self.tit2 = Label(self.frame2,text = "CHOOSE PAYMENT METHOD ",font=("serif",15,"bold")).place(x=320,y= 330)
        self.chcbutn5 = Checkbutton(self.frame2,text = "BY CASH",width =20,height=2, font = ("serif",15,"bold"),variable =self.var5).grid(row=6,pady=20)
        self.chcbutn6 = Checkbutton(self.frame2,text = "BY CREDIT / DEBIT CARD",width =20,height=2, font = ("serif",15,"bold"),variable =self.var6).grid(row=6,column=1,pady=20)
        self.submitbutt =  Button(self.frame2,text = "SUBMIT",height = 4,bg = "Lightgray",width =8,font = ("serif",15,"bold"),fg = "black",command = submit)
        self.submitbutt.place(x=850,y=230)

        root.mainloop()
Hotel()
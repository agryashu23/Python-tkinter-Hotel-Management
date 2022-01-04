from tkinter import *


p = '''
------------ PROJECTWORLDS HOTEL AND RESORTS  ------------
------------ BHILAI CHHATTISGARH  -----------------
------------ SERVING    GUEST   SINCE  2019---------
                                                                                        
  \t\t \t\t\t\t  \t \t \t Contact No. 6232446830
-------------------------------------------------------------------------------------------------------------------
'''

fo1=open("recipt.txt","r")
list1=fo1.readlines()

class receipt:
    def __init__(self):

        root = Tk()
        root.title("Receipt".center(300))
        root.geometry("1080x720")
        root.configure(bg="silver", highlightbackground="gray")
        self.Label1 = Label(root,text = "Thank You!! For Visiting us",fg = "blue",font =("alegerian",25)).pack(pady=5)
        self.Label2 = Label(root, text=p, fg="red",bg= "white", font=("alegerian", 15)).pack()
        self.Label3 = Label(root, text= " NAME: -" + list1[0] , fg="black", bg="white", font=("arial", 14,'bold')).place(x=150,y=250)
        self.Label4 = Label(root, text=" ADDRESS: -" + list1[1], fg="black", bg="white", font=("arial", 14,'bold')).place(x=150,y=300)
        self.Label5 = Label(root, text=" MOBILE NO.: -" + list1[2], fg="black", bg="white", font=("arial", 14,'bold')).place(x=150,y=350)
        self.Label6 = Label(root, text=" ROOM NO -" + list1[3] , fg="black", bg="white", font=("arial", 14,'bold')).place(x=150,y=400)
        self.Label7 = Label(root, text=" TOTAL BILL: -" + list1[4], fg="black", bg="white", font=("arial", 14,'bold')).place(x=150,y=450)











        root.mainloop()










receipt()
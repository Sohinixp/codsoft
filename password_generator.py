import random
import string
from tkinter import*
root=Tk()
root.geometry("655x423")
root.resizable(False,False)
root.title("Password Generator")
root.wm_iconbitmap("icon2.png")


def accept():
    f=open("document.txt","a")
    f.truncate(0)
    f.write(f"{ user_value.get()}")
    f.write("\t-\t")
    f.write(f"{pass_value.get()}")
    f.write("\n")

    pass_value.set("")
    user_value.set("")
    len_value.set("")

def generate():
        k=int(len_value.get())
        all_characters = string.ascii_letters + string.digits + string.punctuation
        pass_value.set(''.join(random.sample(all_characters, k)))

def reset():
      pass_value.set("")


#Creating Labels
Label(root,text="Password Generator",font="algerian 20 bold underline",fg="blue4",pady=7).place(x=176,y=7)
user=Label(root,text="Enter Username:",font="georgia 12",pady=15).place(x=40,y=48)
l=Label(root,text="Enter Password Length:",font="georgia 12",pady=15).place(x=20,y=100)
passwd=Label(root,text="Generated Password:",font="georgia 12",pady=15).place(x=30,y=148)

#Creating Entry Widgets
user_value=StringVar()
len_value=StringVar()
pass_value=StringVar()

user_entry=Entry(root,textvariable=user_value,bd=4,relief=RIDGE).place(x=208,y=60,height=35,width=249)
len_entry=Entry(root,textvariable=len_value,bd=4,relief=RIDGE).place(x=208,y=110,height=35,width=249)
pass_entry=Entry(root,textvariable=pass_value,bd=4,relief=RIDGE).place(x=208,y=160,height=35,width=249)

#Creating Buttons
bttn_border1=Frame(root,highlightbackground="black",highlightthickness=3).place(x=249,y=218,height=49,width=198)
bttn_border2=Frame(root,highlightbackground="black",highlightthickness=3).place(x=293,y=278,height=49,width=81)
bttn_border3=Frame(root,highlightbackground="black",highlightthickness=3).place(x=298,y=338,height=49,width=69)

passwd=Button(bttn_border1,text="GENERATE PASSWORD",fg="blue4",font="georgia 12",pady=7,command=generate).place(x=252,y=220)
acpt=Button(bttn_border2,text="ACCEPT",fg="blue4",font="georgia 12",pady=7,command=accept).place(x=296,y=280)
rst=Button(bttn_border3,text="RESET",fg="blue4",font="georgia 12",pady=7,command=reset).place(x=301,y=340)


root.mainloop()

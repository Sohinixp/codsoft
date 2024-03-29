from tkinter import*
root=Tk()
root.geometry("655x423")
root.resizable(True,False)
root.title("ToDo List")
root.wm_iconbitmap("icon1.jpg")


def getvals():
    global itemvalue
    text=itemvalue.get()
    if text!="" and text!=" ":
        list.insert(END,text)
        itemvalue.set("")
        item_entry.update()
cb=Checkbutton(root)
cb.place(x=300)
        
def delete():
    list.get(ACTIVE)
    list.delete(ACTIVE)

def edit():
    i=list.curselection()
    if i:
         new_task=itemvalue.get()
         if new_task:
             list.delete(i)
             list.insert(i,new_task)
             itemvalue.set("")
             item_entry.update()


#Creating Heading
Label(root,text="ToDo List",font="forte 24 bold",bg="skyblue", fg="black",pady=20).pack(fill=X)
l1=Label(root,text="Add Items-->",font="algerian 14 bold")
l1.place(x=18,y=90)

#Creating a frame for the Add Items Entry Widget
itemvalue=StringVar()
item_entry=Entry(root,textvariable=itemvalue,font="georgia 10")
item_entry.place(x=18,y=125,width=322,height=30)

#Buttons
b1=Button(root,text="Submit",fg="white",bg="red",command=getvals)
b1.place(x=350,y=125,height=27)

b2=Button(root,text="Edit",bg="red",fg="white",pady=20,padx=30,command=edit)
b2.place(x=100,y=350,width=50,height=27)
b3=Button(root,text="Delete",bg="red",fg="white",pady=20,command=delete)
b3.place(x=198,y=350,width=45,height=27)


l2=Label(root,text="Tasks-->", font="algerian 14 bold")
l2.place(x=18,y=170)

#ListBox with ScrollBar
scroll=Scrollbar(root)
scroll.pack(fill=Y,side=RIGHT)

list=Listbox(root,font="georgia 10")
list.place(x=18,y=200,height=130,width=322)
list.config(yscrollcommand=scroll.set)
scroll.config(command=list.yview)

root.mainloop()
import math
from tkinter import*
root=Tk()
root.geometry("464x538")
root.resizable(False,False)
root.title("Calculator")

def calculate(symbol):
    if symbol == "=":
        value=eval(scvalue.get())
        scvalue.set(value)
    elif symbol == "√":
        value= float(scvalue.get())
        scvalue.set(math.sqrt(value))
    elif symbol == "C":
        scvalue.set("")
    elif symbol == "<--":
        value = str(scvalue.get())
        scvalue.set(value.rstrip(value[-1])) 
    elif symbol == "!":
        pass
    else:
        scvalue.set(scvalue.get()+symbol)
    


#Creating Frame
f=Frame(root,bg="grey").pack()

#Entry Widget
scvalue=StringVar()
screen=Entry(f,textvariable=scvalue,font="cascadia 16 bold",bd=7,relief=RIDGE).place(x=20,y=20,width=424,height=50)

#Creating Buttons
b=Button(f,text="C",font="georgia 18 bold",command=lambda:calculate("C")).place(x=20,y=96)
b=Button(f,text="√",font="georgia 18 bold",command=lambda:calculate("√")).place(x=130,y=96)
b=Button(f,text="/",font="georgia 18 bold",command=lambda:calculate("/")).place(x=242,y=96)
b=Button(f,text="<--",font="georgia 18 bold",command=lambda:calculate("<--")).place(x=350,y=96)


b=Button(f,text="7",font="georgia 18 bold",command=lambda:calculate("7")).place(x=20,y=175)
b=Button(f,text="8",font="georgia 18 bold",command=lambda:calculate("8")).place(x=130,y=175)
b=Button(f,text="9",font="georgia 18 bold",command=lambda:calculate("9")).place(x=240,y=175)
b=Button(f,text="*",font="georgia 18 bold",command=lambda:calculate("*")).place(x=364,y=175)


b=Button(f,text="4",font="georgia 18 bold",command=lambda:calculate("4")).place(x=20,y=249)
b=Button(f,text="5",font="georgia 18 bold",command=lambda:calculate("5")).place(x=130,y=249)
b=Button(f,text="6",font="georgia 18 bold",command=lambda:calculate("6")).place(x=240,y=249)
b=Button(f,text="-",font="georgia 18 bold",command=lambda:calculate("-")).place(x=366,y=249)


b=Button(f,text="1",font="georgia 18 bold",command=lambda:calculate("1")).place(x=20,y=328)
b=Button(f,text="2",font="georgia 18 bold",command=lambda:calculate("2")).place(x=130,y=328)
b=Button(f,text="3",font="georgia 18 bold",command=lambda:calculate("3")).place(x=240,y=328)
b=Button(f,text="+",font="georgia 18 bold",command=lambda:calculate("+")).place(x=358,y=328)


b=Button(f,text="!",font="georgia 18 bold",command=lambda:calculate("!")).place(x=20,y=407)
b=Button(f,text="0",font="georgia 18 bold",command=lambda:calculate("0")).place(x=130,y=407)
b=Button(f,text=".",font="georgia 18 bold",command=lambda:calculate(".")).place(x=243,y=407)
b=Button(f,text="=",font="georgia 18 bold",command=lambda:calculate("=")).place(x=359,y=407)


root.mainloop()
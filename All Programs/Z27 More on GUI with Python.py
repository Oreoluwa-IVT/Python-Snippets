#Using Buttons
from tkinter import *


okay=Tk()
okay.title("Buttons Pusher")
okay.geometry("400x300")
now=Frame(okay) # the frame works by placing the object of the class of the moudle tkinter in the class
now.grid()
lbl=Label(now,text="Push the Buttons and see what happens".upper())
lbl.grid() #remember every widget needs to use the grid method

but=Button(now,text="1")
but.grid()

but2=Button(now)
but2.grid()
but2.configure(text="34") # this allows you modify the value of a widget after it has been created

but3=Button(okay) # this meand button will be created in "okay"
but3.grid()
but3["text"]="443"

okay.mainloop()

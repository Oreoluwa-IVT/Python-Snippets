#GUIs in Python
# GUI is event driven
#event handler is a code that runs when and event occurs

#The event loop is simply a term that refers to a part of the program 
#that loop untill and event occurs.
#Note: Root Windows are the foundation of your GUI program
#Simple GUI
#Demonstrates creating a window
from tkinter import *

#to create a root window
#use an object from the Tk() class

root =Tk() # Tk() is a class in the tkinter module. notice that you didn't have to type tkinter.Tk() for it to work. tkinter comdule works like that
#modify the window
root.title("Basic Calculator") # this sets the title of the window 
root.geometry("1000x600") #this sets the size of a root window


#Note: GUI elements are called widgets
#Note: Widgets stands for Windows Gadgets
#An example of a widget is a label widget

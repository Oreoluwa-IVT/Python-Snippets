#Building GUI with a class 

from tkinter import *
class Myapp(Frame):
    """A GUI application with three buttons"""
    def __init__(self,master):
        """Initialize the Frame"""
        super(Myapp,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons that do nothing"""
        #Create the first button 
        self.button1=Button(self,text="Refresh")
        self.button1.grid()

        self.button2=Button(self,text="Search")
        self.button2.grid()

        self.button=Button(self,text="Plot")
        self.button.grid()

        self.button4=Button(self)
        self.button4.grid()
        self.button4["text"] = "Close Window"

        
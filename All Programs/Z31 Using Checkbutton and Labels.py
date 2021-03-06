#Using Radio button in Python
from tkinter import *

class Application(Frame):
    """GUI Application for favourite movie types."""

    def __init__(self,master):
        super(Application,self).__init__(master)
        self.create_widget()
        self.grid()

    def create_widget(self):
        """Create widgets for movie type choices"""

        #Create dscription label

        Label(self,text="Select your Favourite Series").grid(row=0,column=0,sticky=W)
        Label(self,text="Select all that apply").grid(row=1,column=0,sticky=W)


        #note, when creating butttons , you must first instantiate a BoolenaVar object
        #BooleanVar simply means something beign true or false.

        self.likes_comedy=BooleanVar()

        Checkbutton(self,text="Comedy",variable=self.likes_comedy,command=self.update_text).grid(row=2,column=0,sticky=W)
        #the command simply allows bind the self.update_text method to it . When the user clicks , update_text() method is invoked
        #variable simply helps associate the nature of the checkbutton to be like a Boolean (True of False)
        #variable helps us take not of the status of the button. that's also why "Checkbuttonn" is not assigned to variable s


        self.likes_drama=BooleanVar()
        Checkbutton(self,text="Drama",variable=self.likes_drama,command=self.update_text).grid(row=3,column=0,sticky=W)

        self.likes_romance=BooleanVar()
        Checkbutton(self,text="Romance",variable=self.likes_romance,command=self.update_text).grid(row=4,column=0,sticky=W)

        self.results_txt=Text(self,width=40,height=5,wrap=WORD)
        self.results_txt.grid(row=5,column=0, columnspan=3)
    
    def update_text(self):
        """Update text widget and display user's favorite movie types."""
        
        likes=""

        if self.likes_comedy.get():
            likes+="you Like comedic movies \n"

        if self.likes_drama.get():
            likes+="you like dramatic movies. \n"

        if self.likes_romance.get():
            likes+="you like romantic movies."

        self.results_txt.delete(0.0,END)
        self.results_txt.insert(0.0,likes)

#main program
root=Tk()
root.title("Series Selector")
root.geometry("300x200")
app=Application(root)
root.mainloop()





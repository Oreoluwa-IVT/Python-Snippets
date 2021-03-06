#using radio button 
#unlike checkboxes, radio button allow you to make one selection at a time

from tkinter import *


class Application(Frame):
    """GUI with radio button"""
    def __init__(self,master):
        """this is the constructor"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    
    def create_widget(self):
        """Create the first label"""
        Label(self,text="Choose your Favorite Stack").grid(row=0,column=0,sticky=W)
        Label(self,text="Select One").grid(row=1,column=0,sticky=W)

        # because these are radio button,there are special objects that tells us if a radio buttion is checked 
        # this objects have to be objects of the StringVar class from the tkinter module.

        # note: we set the initial value of the radio button to None


        self.favorite=StringVar()
        self.favorite.set(None)

        Radiobutton(self,text="Web Developer",variable=self.favorite,value="PHP,Javascript, HTML, CSS, Vue.js.",command=self.update_text).grid(row=2,column=0,sticky=W)

        # the variable option defines the special variable associated with the radio button  "self.favorite"
        # the value option defines the value that should be stored by the special variable when the radio button is selected
        # this simply means, once the radio button is selected, StringVar referenced by self.favorite will store the string "comedy"
        # In simply terms . One the button is click , StringVar will store the specified value.

        Radiobutton(self,text="Mobile App Developer",variable=self.favorite,value="Flutter, JSON, Mysql,Firebase",command=self.update_text).grid(row=3,column=0,sticky=W)
        Radiobutton(self,text="Web App Developer",variable=self.favorite,value="C#, HTML, CSS, Javascript",command=self.update_text).grid(row=4,column=0,sticky=W)

        self.result_txt=Text(self,width=85,height=5,wrap=WORD)
        self.result_txt.grid(row=5,column=0, columnspan=3)


        # To get the value from a radio button, we have to instantiate the get() method prseent in the StrinVar() class


    def update_text(self):
        """Update text area and display user's favorite movie types."""
        message="You Code in "
        message+=self.favorite.get() # remember StringVar stores the value of the radio button and it is referrenced by self.favorite. that's why the get 
        #method is attached to self.favorite.

        self.result_txt.delete(0.0,END)
        self.result_txt.insert(0.0,message)




#main
root = Tk()
root.title("Movie Choose")
root.geometry("500x300")

app = Application(root)
root.mainloop()




#Oluwafemi Oreoluwa Adetoro
#2021
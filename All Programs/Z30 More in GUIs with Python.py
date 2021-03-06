#Working with Text, entry and grid layout manager widgets
#Longevity 

from tkinter import  *

class Application(Frame):
    """GUI application which can reveal"""
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        """Create button , text , and entry widgets."""

        #Create instructions Label
        self.inst_lbl= Label(self,text="Enter Password for the secrt of longevity")
        self.inst_lbl.grid(row=0,column=0,columnspan=2,sticky=W)
        self.pw_lbl=Label(self,text="Password")
        self.pw_lbl.grid(row=1,column=0,sticky=W)

        # note that the coloumn span attribute, simply increases the column based on the integer you give it 
        # note that the row span attribute, simply increases the row based on the intergrer you give it
        # create entry widget to accept password

        self.pw_ent=Entry(self)  # this is how to create a text entry widget
        self.pw_ent.grid(row=2,column=1,sticky=W)

        #create submit button
        self.submit_bttn=Button(self,text="Submit",command=self.reveal) # remember that Button takes the self reference ,text and can also take "command"
        self.submit_bttn.grid(row=3,column=3)
        self.secret_txt=Text(self,width=35 , height =5, wrap = WORD) # this is to create the text display widget
        self.secret_txt.grid(row=3,column=0,columnspan=2,sticky=W)
        # reveal is simply a method that binds the  Submit button
    
    def reveal(self):
        """Display message based on password."""
        contents=self.pw_ent.get()# in this part of the code , we simply used the "get()" method to pull the text for Entry "which is a text widget", then assign it to contents
        if contents =="secret":
            message="Here's the secret to living to 100: Live to 99 and then be very careful"
        
        else:
            message="That's not the correct password, so I can't share the secret with you"

        self.secret_txt.delete(0.0,END)
        # note , the delete method take in a begining column and an end column to delete
        self.secret_txt.insert(0.0,message)
        #this insert method, can insert a string into a text widget+


#main
root=Tk()
root.title("The Secret to Life")
root.geometry("400x300")

app=Application(root)

root.mainloop()

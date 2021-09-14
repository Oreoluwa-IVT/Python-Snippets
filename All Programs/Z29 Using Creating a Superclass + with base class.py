#Event Handlers with Python
# We are going to create a button event handler that shows us how many times a button has been clicked


from tkinter import *

class Application(Frame):
    """GUI app application which counts button clicks."""
    def __init__(self,master):
        """Initialize the frame"""
        super(Application,self).__init__(master)
        self.grid()
        self.bttn_clicks =0  # this is simply and object attribute to keep track of the number of times we click 
        self.create_widget() # here we simply place "create_widget" here because we want the button to be create as soon as the class is instantiated

# we are about to create an event handler
    
    def create_widget(self):
        """Create button which displays number of cities"""
        self.bttn=Button(self) # in this part of the program, I use self as the master for the button so that application object is their master
        self.bttn["text"]="Number of times 0"
        self.bttn["command"]=self.update_count # when the user click the Button , the method "update_count " is invoked
        # note that you have to se ta widget's commmand to bind the activation of the widget with an event handler.
        self.bttn.grid()
    
    def update_count(self):
        """Increase click count and display new total"""
        self.bttn_clicks +=1
        self.bttn["text"]="Total Clicks: "+ str(self.bttn_clicks)


    



#main
root=Tk()
root.title("Click Counter")
root.geometry("400x100")
app=Application(root)

root.mainloop()

    
        



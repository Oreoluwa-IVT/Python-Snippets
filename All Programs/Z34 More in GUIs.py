#Mad Lib
#Create a story based on user input

from tkinter import *


class Application(Frame):
    """GUI application that creates a story based on user input"""
    def __init__(self,master):
        """this is a constructor"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        """Create widgets to get story information and to display story"""
        #Create instruction label

        Label(self, text="Enter information for a new story").grid(row=0,column=0,columnspan=2, sticky=W)
        
        #Create a Label and text entry for the name of a person
        Label(self,text="Person:").grid(row=1,column=0,sticky=W)

        self.person_ent=Entry(self) # this is how we start an entry textbox
        self.person_ent.grid(row=1,column=1,sticky=W)

        #create a label and text entry for a plural noun
        Label(self,text="Plural Noun").grid(row=2,column=0,sticky=W)

        self.noun_ent=Entry(self)# this is how we start an entry textbox. then we use the get() method to pull the text from the textbox
        self.noun_ent.grid(row=2,column=1,sticky=W)

        # create a label and text entry for a verb

        Label(self,text="Verb:").grid(row=3,column=0,sticky=W)
        self.verb_ent=Entry(self)
        self.verb_ent.grid(row=3,column=1,sticky=W)

        #create a Label for adjectives check buttons
        Label(self,text="Adjective(s)").grid(row=4,column=0,sticky=W)

        #create itchy check button
        self.is_itchy=BooleanVar() # this help the Checkbutton know that it's either choosing true or false
        Checkbutton(self,text="itchy",variable=self.is_itchy).grid(row=4,column=2,sticky=W)


        #Create electric check button
        self.is_electric=BooleanVar()
        Checkbutton(self,text="electric",variable=self.is_electric).grid(row=4,column=3,sticky=W)

        #Create a label for body parts radio buttons
        Label(self,text="Body Part:").grid(row=5,column=0,sticky=W)

        #Create variable for single body part
        self.body_part = StringVar()
        self.body_part.set(None)

        #Create body part radio buttons
        body_part=["bellybutton","big toe","medulla oblongata"]
        column=1
        for part in body_part:
            Radiobutton(self,text=part,variable=self.body_part,value=part).grid(row=5,column=column,sticky=W)
            column+=1

        #create a submit button
        Button(self,text="Click for story",command=self.tell_story).grid(row=6,column=0,sticky=W)
        # ever button should have something its going to do , this si the command section

        self.story_txt = Text(self,width=76,height=10,wrap=WORD)
        self.story_txt.grid(row=7,column=0,columnspan=4)


    def tell_story(self):
        """Fill textbox box with new story based onuse input."""

        #get values from the GUI
        person=self.person_ent.get()
        noun=self.noun_ent.get()
        verb=self.verb_ent.get()

        adjectives=""
        if self.is_itchy.get():
            adjectives +="itchy."

        if self.is_joyous.get():
            adjectives +="joyous"
            
        if self.is_electric.get():
            adjectives+="electric."

        body_part=self.body_part.get()

        story+="The Famous Explorer"
        story+=person
        story+="had nearly given up a life long quest to find The Lost City of"
        story+=noun.title()
        story+="When one day, the"
        story+=noun
        story+="found"
        story+=person + ","
        story+="A Strong"
        story+=adjectives
        story+="Peculiar feeling overwhelmed the explorer."
        story+="After all this time, the quest was finally over, A tear came to"
        story+=person +"'s"
        story+=body_part +","
        story+="And then, the"
        story+=noun
        story+="promptly devoured"
        story+=person +","
        story+="The moral of the story ? Be careful  what you"
        story+=verb
        story+=" for,"

        #display the story
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0,story)

        

#main
root=Tk()
root.title("New GUI")
app=Application(root)
root.mainloop()









#Oluwafemi Oreoluwa Adetoro
#2021
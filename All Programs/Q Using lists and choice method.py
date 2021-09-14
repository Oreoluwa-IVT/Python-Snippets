# This is a prgram that prints out a list of names and then deletes the elememnts it randomly printed
import random
okay=["Dog","Mouse","Cow","goat","Hen"]
number=len(okay)
numberr=0
while numberr !=number:
    data=random.choice(okay)
    print(data)
    okay.remove(data)
    numberr+=1
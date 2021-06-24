#Hero's Inventory 3.0
#Demonstrates lists 
import random

#create a list with some items and display with a for loop
inventory=["sword","armor","shield","healing potion"]

turple2=["Oreoluwa","Ayomikun","Oghale","Johnson","Paul"]
inventory+=turple2

print(inventory)

inventory[3]="Jammy Vardy"

# note that you can delete a list . All you have to do is use the del opertor follow by the element index

del inventory[3]
del inventory[0:4]

print(inventory)

letters=random.choice(inventory)
print(letters)


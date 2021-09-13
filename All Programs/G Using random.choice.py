#Creating a whole new tuple 
inventory=("sword","armor","shield","healing potion")
#print the tuple 
print("\nThe tuple inventory is:")

print(inventory)

#print each element in the tuple
print("\nYour items:")


for items in inventory:
    print(items)


print("The length of your inventory is equal to", len(inventory))

if "sword" in inventory:
    print("Sure it's in there")
else:
    print("\n\nNo it's not")


print("In this part of the program, we are going to be indexing tuples")
print(inventory[2])

print("In this part of the program, we are going to be slicing the tuple just like strings")
print(inventory[0:3])


#inventory[0]="Oreoluwa" dont bother doing this because tuples are immutable


#NOte that you cannot change the element in a turple but you can add elemets to a tuple 
#for example 

chest=("stomach","tummy")
inventory+=chest
print(inventory)


# this is how to use the random.range for turples . Simply use random.choice(NAME OF TUPLE)
import random
print(random.choice(inventory))




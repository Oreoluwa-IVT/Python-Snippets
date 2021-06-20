geek={"Monkey":"This is an mamal that walk on two legs and look like a man",
"Bannana":"This is a fruit that's very nutritious, monkey love it. It is usually yellow in color",
"Dog":"This is a mamal that walks on two legs"}

letter=input("Please search for a word")
if letter not in geek:
    definition=input("Can you tell us what it mean please ?")
    geek[letter]=definition # this park of the code assigns the variable "definition" as a value to the word entered initially being represented as a key
    print("\n\n",letter,": ",geek[letter])

print(geek.keys())
print(geek.values())
print(geek.items())

import random
thiis=("this ","second","third")
print(thiis[0])
print(random.choice(thiis))

    # would you like to deleta term
odelete=input("\n\nwould you like to delete a term in the dictionary ? so type the term")
if delete in geek:
    input("Press enter to delete the word from your dictionary")
    del geek[delete]
    print("\n\n",delete,"has been deleted")
    inputt=input("Search the word to confirm ")
    print(geek.get(inputt,"Nope it's not there")) # the get method simply help to check for terms, if the team doesn't exist , it prints out the second parameter state in the method




#Greek Translator
#Demonstrates using dictionaires
geek={"404":"clueles, from the web error message 404. meaning page not found.","Googling":"searching the internet for background information on a person",
"Keyboard Plaque":"the collection of debris found in coumputer keyboards.","link rot":"the process by which web page links become obsolete",
"percussive maintenance":"the act of striking an eletronic device to make"}



print(geek["Keyboard Plaque"])
print(geek["percussive maintenance"])

#dictonairees dont have postition number at all # dictornaties don't have positio number

#dictionaries dont' have position number number at all 

if "oreoluwa" in geek:
    print("Yes it is there")

else:
    print("isn't in geek") 

print(geek.get("404","I have no idea"))

# this function is used to fetching a vlaue of a key 
#if the key you're seaching for isn't ther it prints out the exeception that your createsd

# here is what happens when you dont' supply and exceiption value, you acutally get None back


print(geek.get("Dancing baloney"))
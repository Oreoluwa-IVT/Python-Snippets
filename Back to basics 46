#using shelves this time

import shelve
file=shelve.open("C:\\Users\\Oreoluwa\\Videos\\allnew2.dat") #shelve requires just one argument and that's the 
#filename along with the path, depending on where the directory your pulling the data from
file.sync() # you use sync to make sure the data is written on

file["oreoluwa"]=["Handsome","tall","Smart","industrius","visionary"]
file["elon musk"]=["Epitome of hardwork","White","Ameriacan","Visionary"]
file["Bill gates"]=["Really Smart","Avid reader","Ex CEO Microsoft"]

print(file["oreoluwa"])
#Working with pickles and shelves
import pickle, shelve
#first we have to write into the file , Remember initially the file doesn't exist so the "wb" creates the file if it doesn't already exist
f=open("C:\\Users\\Oreoluwa\\Videos\\allnew.dat","wb")
variant=["new","old","newer","older"]
another_variant=["little","bit","large","Verylarge"]
newnew=pickle.dump(variant,f)

#Now we want to read from that file. For us to do that, we use the "rb" and load from the variable assigned to the file initially.
f=open("C:\\Users\\Oreoluwa\\Videos\\allnew.dat","rb")
now=pickle.load(f)

print("\n\n\nYou have successfully pickles and loaded this: ",end="")
print(now)
f.close()

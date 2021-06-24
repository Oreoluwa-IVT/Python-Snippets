#Oreoluwa's Python Practice File 
#Read it 
#Demonstrates reading from a text file

print("Opening and closing file.")
text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
text_file.close()


print("\nReading characters from the file.")
text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
print(text_file.read(1))
print(text_file.read(5))

text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
whole_thing=text_file.read()
print(whole_thing)
text_file.close()

print("\nReading characters from a line")
text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
lines=text_file.readlines()

print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()


print("\nLooping through the file,line by fine")
text_file=open("C:\\Users\\Oreoluwa\\Videos\\read_it.txt","r")
for line in text_file:
    print(line)
text_file.close()


input("\n\nPress the enter key to exit")




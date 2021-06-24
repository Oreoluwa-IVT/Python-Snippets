#Pizza Slicer
#Demonstrates string Slicing 

word="pizza"

print("""Slicing 'Cheat Sheet'""")
print("Enter the beginneing and ending index for your slice of 'pizza'.")
print("Press the enter key at 'Start' to exit.")

start=None
while start !="":
    start=(input("\nStart:"))
    if start:
        start=int(start)
        finish=int(input("Finish:"))
        print("word[",start,":",finish,"] is",end="")
        print(word[start:finish])

input("\n\nPress the enter key exit.")
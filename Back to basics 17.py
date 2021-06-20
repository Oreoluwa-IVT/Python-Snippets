#Welcome to the count program
import random 
response=""
while response !="okay":
    newnumber=int(input("Enter the first number to count from"))
    oldnumber=int(input("Enter the second number to count from"))
    shift=int(input("By how much do you want to shift the count for"))
    for i in range(newnumber,oldnumber,shift):
        print(i," ",end="")
        
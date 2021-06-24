#Demonstrates the break and continue statements 
#Finicky Counter

count=0
while True:
    count+=1
    if count >10:
        break
    if count== 5:
        continue
    print(count)

input("\n\nPress the enter key to exit")




#end loop if count greater than 10
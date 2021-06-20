#High Scores 
#Demostrates list methods 

scores=[]


response=5
while response !=0:
    enter=input("enter a new value")
    scores.append(enter)
    response-=1


print("Now look",scores)

scores.remove(scores[2])
print(scores)
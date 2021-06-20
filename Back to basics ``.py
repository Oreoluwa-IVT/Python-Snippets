# the fortune Cookie Program
print("You are welcome to the fortune cookie program,"\
    "select between 1 and 5 to see your fortune from the cookie")

import random
cookie=random.randint(0,6)
number1="\n\nYou are goind to be very successful in the future"
number2="\n\nThings will always work out for you in grand style as long as you put God first and do the work"
number3="\n\n10 Cars will be bought for you on your 40th Birthday"
number4="You will have a very sharp memory in your 20s down to yout 100s if you put the data in your mind to heart"
number5="You are going to have 2 Children 1 Girl and 1 Boy"

inpuut=int(input("Enter a number to see your fortune"))
if inpuut==1:
    print(number1)
elif inpuut==2:
    print(number2)
elif inpuut==3:
    print(number3)
elif inpuut==4:
    print(number4)
elif inpuut==5:
    print(number5)
else:
    print("\n\nI'm not sure that number is amongst your foutune")


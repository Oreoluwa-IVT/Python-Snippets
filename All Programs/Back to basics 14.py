#input
respond=""
vowels="aeiou"
message=input("The Text")

for letters in vowels:
    if letters in message:
        message+=vowels
        print("Your message is",message)
        


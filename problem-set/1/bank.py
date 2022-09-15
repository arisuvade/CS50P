forbidden_letter = "h"
greeting = input("Greeting: ")

if greeting == "hello":
    print("$0")
elif greeting >= forbidden_letter:
    print("$20")
else:
    print("$100")

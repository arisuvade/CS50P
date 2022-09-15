forbidden_letter = "h"
forbidden_greeting = "hello"
greeting = input("Greeting: ")

if greeting == "hello":
    print("$0")
elif greeting >= forbidden_greeting:
    print("$0")
elif greeting >= forbidden_letter:
    print("$20")
else:
    print("$100")

print("chatbot started")
print("type 'bye' to exit")

while True:
    
    message = input("you: ").lower()

    if "hello" in message or "hi" in message or "hey" in message:
        print("hi buddy")

    elif "how are you" in message or "hru" in message or "how r u" in message:
        print("I'm fine")
        
    else:
        print("sorry i don't under stand")

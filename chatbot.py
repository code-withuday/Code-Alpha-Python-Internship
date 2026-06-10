print("chatbot started")
print("type 'bye' to exit")

while True:
    
    message = input("you: ").lower()

    if "hello" in message:
        print("hi buddy")

    elif "how are you" in message:
        print("I'm fine")
        
    else:
        print("i don't know")
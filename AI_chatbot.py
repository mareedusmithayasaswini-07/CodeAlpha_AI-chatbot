# Task 2: Basic Chatbot
# Simple rule-based chatbot using Python

def chatbot():

    print("----- Welcome to Simple Chatbot -----")
    print("Type 'bye' to end the chat\n")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi!")

        elif message == "how are you":
            print("Bot: I'm fine, thanks!")

        elif message == "what is your name":
            print("Bot: My name is ChatBot.")

        elif message == "who created you":
            print("Bot: I was created using Python.")

        elif message == "good morning":
            print("Bot: Good morning! Have a nice day.")

        elif message == "good afternoon":
            print("Bot: Good afternoon!")

        elif message == "good evening":
            print("Bot: Good evening!")

        elif message == "what are you doing":
            print("Bot: I am chatting with you.")

        elif message == "where are you from":
            print("Bot: I live inside a Python program.")

        elif message == "what can you do":
            print("Bot: I can answer simple questions.")

        elif message == "tell me a joke":
            print("Bot: Why do programmers hate nature? Too many bugs.")

        elif message == "tell me something":
            print("Bot: Python is one of the most popular programming languages.")

        elif message == "favorite color":
            print("Bot: I like blue.")

        elif message == "favorite food":
            print("Bot: I don't eat food, but pizza sounds good.")

        elif message == "do you like coding":
            print("Bot: Yes, coding is interesting.")

        elif message == "what day is today":
            print("Bot: Sorry, I cannot check the date.")

        elif message == "are you a robot":
            print("Bot: Yes, I am a simple chatbot.")

        elif message == "i am sad":
            print("Bot: I hope things get better for you.")

        elif message == "i am happy":
            print("Bot: That's great to hear!")

        elif message == "thank you":
            print("Bot: You're welcome!")

        elif message == "thanks":
            print("Bot: Happy to help!")

        elif message == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Calling the chatbot function
chatbot()
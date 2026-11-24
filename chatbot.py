def get_response(user_input):
    """Return a predefined reply based on the user's message."""
    # Normalize the input: remove extra spaces, ignore capitalization and trailing punctuation
    message = user_input.strip().lower().strip("?!.")

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("bye", "goodbye"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that yet."


def chat():
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        # Stop the loop once the chatbot has said goodbye
        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    chat()

def simple_chatbot(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Define some rules and responses
    rules = {
        "hi": "Hello!",
        "how are you": "I'm good, thank you!",
        "bye": "Goodbye! Have a nice day."
    }
    
    # Check if user input matches any of the defined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response
    
    # If no match is found, respond with a default message
    return "I'm sorry, I don't understand that."
    
# Test the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    else:
        bot_response = simple_chatbot(user_input)
        print("Chatbot:", bot_response)

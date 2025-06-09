import chatbot

def main():
    
    print("NicBot: Hello there!")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("NicBot: See you later!")
            break
        response = chatbot.get_response(user_input)
        print(f"NicBot: {response}")

if __name__ == "__main__":
    main()
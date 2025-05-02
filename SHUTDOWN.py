def shutdown():

    user_input = input("Do you want to shut down the system? (YES/NO): ").strip().upper()


    if user_input == "YES":
        print("Shutting down...See you later")
    elif user_input == "NO":
        print("Abort.")
    else:
        print("Sorry, I didn't understand your response.Maby try again")

shutdown()

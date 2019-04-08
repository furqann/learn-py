while (True):
    command = input('> ').lower()
    if command == "start":
        print("Car started")
    elif command == "stop":
        print("Car stopped")
    elif command == "quit":
        break
    elif command == "help":
        print("""
Start the car type start
Stop the car type stop
Quit the game type quit
        """)
    else:
        print("I don't understand that...")
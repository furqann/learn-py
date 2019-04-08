last_command = ""
while (True):
    command = input('> ').lower()
    if command == "start":
        if last_command != "start":
            print("Car started")
            last_command = "start"
        else:
            print("Car is already started")
    elif command == "stop":
        if last_command != "stop":
            last_command = "stop"
            print("Car stopped")
        else:
            print("Car is already stopped")
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
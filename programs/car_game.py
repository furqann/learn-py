is_started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if is_started:
            print("Car is already started")
        else:
            print("Car started")
            is_started = True
    elif command == "stop":
        if not is_started:
            print("Car is already stopped")
        else:
            print("Car stopped")
            is_started = False
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

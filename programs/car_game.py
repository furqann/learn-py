help = input("")
if help.lower() == "help":
    print("Start the car type start")
    print("Stop the car type stop")
    print("Quit the game type quit")
    choice = input()
    while (True):
        if choice.lower() == "start":
            print("Car started")
        elif choice.lower() == "stop":
            print("Car stopped")
        elif choice.lower() == "quit":
            print("Quiting")
            break
        else:
            print("I don't understand that...")
        choice = input()
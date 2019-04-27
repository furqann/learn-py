#  https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

rock = 1
scissor = 2
paper = 3


def main_menu():
    print("""
    Please Select 
        1. Rock 
        2. Scissor 
        3. Paper
    """)


def check_who_wins(player_1, player_2):
    if player_1 == player_2:
        print("Draw!!")
    elif player_1 == scissor and player_2 == rock:
        print("Player 2 wins!")
    elif player_1 == rock and player_2 == paper:
        print("Player 2 wins!")
    elif player_1 == paper and player_2 == scissor:
        print("Player 2 wins!")
    else:
        print("Player 1 wins!")


def take_input(player_name):
    try:
        user_input = int(input(f"{player_name} player turn: "))
    except ValueError:
        print("Invalid Input")
        take_input(player_name)
    if user_input <= 0 or user_input >= 4:
        print("Wrong selection please select only 1, 2 or 3")
        take_input(player_name)
    return user_input


while True:
    main_menu()
    player_1 = take_input("First")
    player_2 = take_input("Second")
    check_who_wins(player_1, player_2)


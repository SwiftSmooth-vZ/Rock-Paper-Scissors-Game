import random
print("Hello and Welcome, Let's play Rock Paper Scissors!")
def play():
    condition = True
    while condition == True:
        user = input("\nPlease type in 'r' for rock, or 'p' for paper or 's' for scissors: ")
        computer = random.choice(["r", "p", "s"])
        user_choice = ""
        if user == "r":
            user_choice += "rock"
        elif user == "p":
            user_choice += "paper"
        elif user == "s":
            user_choice += "scissors"


        computer_choice = ""
        if computer == "r":
            computer_choice += "rock"
        elif computer == "p":
            computer_choice += "paper"
        elif computer == "s":
            computer_choice += "scissors"



        if user == computer:
            print ("\nIt's a tie.")
            play_more = input("\nWould you like to play again? 'y' for Yes, and 'n' for No: ")
            if play_more == "y":
                condition = True
            elif play_more == "n":
                condition = False
                print("Thanks for playing, hope to see you soon!")
        elif win(user, computer):
            print (f"\nCongratulations you have beaten {computer_choice} with {user_choice}. ")
            play_more = input("\nWould you like to play again? 'y' for Yes, and 'n' for No: ")
            if play_more == "y":
                condition = True
            elif play_more == "n":
                condition = False
                print("\nThanks for playing, hope to see you soon!")
        else:
            print (f"\nUnfortunately your {user_choice} got beaten by {computer_choice}. Good Luck next time.")
            play_more = input("\nWould you like to play again? 'y' for Yes, and 'n' for No: ")
            if play_more == "y":
                condition = True
            elif play_more == "n":
                condition = False
                print("\nThanks for playing, hope to see you soon!")

def win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True

play()
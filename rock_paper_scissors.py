# start the game
# ask the player to make a move (r,p,s)
# pc would select a move randomly
# pc == player => tie
# (player == p and pc == rock ) or (player == r and pc == s) or (player == s and pc == p) => you won !

import random

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
computer_choice = random.choice(choices)

print(f"You chose {user_choice}.")
print(f"Computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("Computer wins!")

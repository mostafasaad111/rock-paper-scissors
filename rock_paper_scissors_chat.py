import random


def get_user_choice():
    while True:
        user = input(
            "What's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: "
        ).lower()
        if user in ["r", "p", "s"]:
            return user
        else:
            print("Invalid input. Please enter 'r', 'p', or 's'.")


def determine_winner(user, pc):
    if user == pc:
        return "It's a tie!"
    elif (
        (user == "p" and pc == "r")
        or (user == "r" and pc == "s")
        or (user == "s" and pc == "p")
    ):
        return "You won!"
    else:
        return "You lose!"


def main():
    user = get_user_choice()
    pc = random.choice(["r", "p", "s"])

    print("PC played: " + pc)
    print("User played: " + user)

    result = determine_winner(user, pc)
    print(result)


if __name__ == "__main__":
    main()

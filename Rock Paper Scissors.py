import random

while True:
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper or scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("It's a draw.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break


import random

print("🎲 Welcome to the Dice Duel 🎲")

while True:
    start = input("Do you want to start the duel? (yes/no): ").lower()

    if start == "yes":
        input("Player 1, press Enter to roll your dice...")
        p1_roll = random.randint(1, 6)
        print("Player 1 rolled:", p1_roll)

        input("Player 2, press Enter to roll your dice...")
        p2_roll = random.randint(1, 6)
        print("Player 2 rolled:", p2_roll)

        if p1_roll > p2_roll:
            print("🔥 Player 1 wins the duel!")
        elif p2_roll > p1_roll:
            print("🔥 Player 2 wins the duel!")
        else:
            print("🤝 It's a tie! Rematch?")

    elif start == "no":
        print("Alright, duel's over. Catch ya later.")
        break

    else:
        print("Say 'yes' or 'no', bruv.")

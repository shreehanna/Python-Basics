import random

# Dice art
def dice_face(value):
    dice_art = {
        1: ["+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"],
        2: ["+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"],
        3: ["+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"],
        4: ["+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"],
        5: ["+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"],
        6: ["+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"]
    }
    return dice_art[value]

# Play one round and return winner
def play_round():
    playerr = random.randint(1, 6)
    compp = random.randint(1, 6)

    player = dice_face(playerr)
    comp = dice_face(compp)

    print(f"\n🎲 Player rolled: {playerr}    CPU rolled: {compp}")
    print("     PLAYER              CPU")
    for p_line, c_line in zip(player, comp):
        print(f"   {p_line}     {c_line}")

    if playerr > compp:
        print("\n🏆 Player wins this round!")
        return "player"
    elif compp == playerr:
        print("\n🤝 It's a tie!")
        return "tie"
    else:
        print("\n💻 CPU wins this round!")
        return "cpu"

# Main game loop
def main():
    player_score = 0
    cpu_score = 0

    print("🎮 Welcome to Dice Duel: Best of 5!")

    while player_score < 3 and cpu_score < 3:
        winner = play_round()

        if winner == "player":
            player_score += 1
        elif winner == "cpu":
            cpu_score += 1

        print(f"\n📊 SCORE → Player: {player_score} | CPU: {cpu_score}\n")

    if player_score == 3:
        print("🎉 Player wins the match!")
    else:
        print("💻 CPU wins the match!")

    print("🏁 Thanks for playing!")

# Only run if this file is executed directly
if __name__ == "__main__":
    main()





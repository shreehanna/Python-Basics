import random

while True:
    roll = input("Wanna roll your dice? (yes/no): ").lower()

    if roll in ["yes"]:
        print("🎲 The system chose:", random.randint(1, 6))
    elif roll in ["no"]:
        print("🚪 Alright... see you soon!")
        break
    else:
        print("😐 Mate... it's either yes or no.")

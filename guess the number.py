import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("🎯 You guessed right!")
        break
    elif guess > num:
        print("📈 Sorry, you guessed higher!")
    else:
        print("📉 Sorry, you guessed lower!")





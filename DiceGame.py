import random

def dice_game():
    print("Rolling the dice...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"You rolled: {dice1} and {dice2}")
    print(f"Total: {dice1 + dice2}")

dice_game()


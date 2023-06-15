import random

while True:
    command = input("Enter command (toss or quit): ")
    if command == "toss":
        dice_roll = random.randint(1, 6)
        print("You rolled a", dice_roll)
    elif command == "quit":
        break
    else:
        print("Invalid input. Please enter either 'toss' or 'quit'") 


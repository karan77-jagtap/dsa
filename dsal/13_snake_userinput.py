import random

# Define the board with snake and ladder positions
# Positive values represent ladders, negative values represent snakes
board = [i for i in range(101)]
# Sample snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

for key, value in snakes.items():
    board[key] = value
for key, value in ladders.items():
    board[key] = value

def roll_dice():
    # Ask the user to provide a dice value between 1 and 6
    while True:
        try:
            roll = int(input("Enter your dice roll (1-6): "))
            if 1 <= roll <= 6:
                return roll
            else:
                print("Please enter a valid dice roll between 1 and 6.")
        except ValueError:
            print("Invalid input, please enter an integer between 1 and 6.")

def play_game():
    position = 1
    while position < 100:
        print(f"\nYou are currently on square {position}")
        dice_roll = roll_dice()
        position += dice_roll
        
        # Check if the player landed on a snake or ladder
        if position < 100:
            if board[position] != position:
                if board[position] > position:
                    print(f"Yay! You climbed a ladder to square {board[position]}")
                else:
                    print(f"Oops! You got bitten by a snake and are now on square {board[position]}")
            position = board[position]
        
        if position >= 100:
            print("Congratulations! You have reached or passed square 100. You win!")
            break

if __name__ == "__main__":
    print("Welcome to Snakes and Ladders!")
    play_game()

import random

snakes = {99: 7, 65: 52, 54: 19, 17: 5, 62: 37, 87: 24, 93: 73}
ladders = {3: 38, 10: 32, 27: 46, 50: 68, 61: 79, 70: 89, 80: 99}

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position):
    while True:
        roll = roll_dice()
        print(f"{player} rolled a {roll}")

        # Move only if not exceeding 100
        if position + roll <= 100:
            position += roll

        # Snake or ladder check
        if position in snakes:
            print(f"{player} got bitten by a snake! Down to {snakes[position]}")
            position = snakes[position]
        elif position in ladders:
            print(f"{player} climbed a ladder! Up to {ladders[position]}")
            position = ladders[position]

        print(f"{player} is now at {position}\n")

        # If not 6, end turn
        if roll != 6:
            break
        else:
            print(f"{player} rolled a 6 and gets another turn!")

    return position

def playgame():
    num_players = int(input("Enter number of players: "))
    players = {f"player {i+1}": 0 for i in range(num_players)}

    while True:
        for player in players:
            input(f"{player}'s turn! Press Enter to roll the dice...")
            players[player] = move_player(player, players[player])
            if players[player] == 100:
                print(f"\n{player} wins the game!\n")
                return

playgame()
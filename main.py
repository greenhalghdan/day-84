
game_board = {
"a1": " ",
"a2": " ",
"a3": " ",
"b1": " ",
"b2": " ",
"b3": " ",
"c1": " ",
"c2": " ",
"c3": " "
}

# game_grid = (f"{game_board['a1']}|{game_board['a2']}|{game_board['a3']}\n"
#             f"- - -\n"
#             f"{game_board['b1']}|{game_board['b2']}|{game_board['b3']}\n"
#             f"- - -\n"
#             f"{game_board['c1']}|{game_board['c2']}|{game_board['c3']}")

def game_grid():
    grid = (f"{game_board['a1']}|{game_board['a2']}|{game_board['a3']}\n"
                 f"- - -\n"
                 f"{game_board['b1']}|{game_board['b2']}|{game_board['b3']}\n"
                 f"- - -\n"
                 f"{game_board['c1']}|{game_board['c2']}|{game_board['c3']}")
    print(grid)
def gameround(player):
    # print(game_grid)
    print(f"its is {player}'s go:")
    player_choosing = True
    while player_choosing:
        choice = input("whats your choice: ")
        # print(game_board[choice])
        if choice not in game_board:
            print("Thats not a valid choice")
        elif game_board[choice] != " ":
            print("That space is already filled")
        else:
            game_board[choice] = player
            player_choosing = False
        # print(game_board[choice])
    return


def isthereawinner():
    if game_board['a1'] == 'x' and game_board['a2'] == 'x' and game_board['a3'] == 'x':
        return False
    elif game_board['a1'] == 'o' and game_board['a2'] == 'o' and game_board['a3'] == 'o':
        return False
    elif game_board['b1'] == 'x' and game_board['b2'] == 'x' and game_board['b3'] == 'x':
        return False
    elif game_board['b1'] == 'o' and game_board['b2'] == 'o' and game_board['b3'] == 'o':
        return False
    elif game_board['c1'] == 'x' and game_board['c2'] == 'x' and game_board['c3'] == 'x':
        return False
    elif game_board['c1'] == 'o' and game_board['c2'] == 'o' and game_board['c3'] == 'o':
        return False
    elif game_board['a1'] == 'x' and game_board['b1'] == 'x' and game_board['c1'] == 'x':
        return False
    elif game_board['a1'] == 'o' and game_board['b1'] == 'o' and game_board['c1'] == 'o':
        return False
    elif game_board['a2'] == 'x' and game_board['b2'] == 'x' and game_board['c2'] == 'x':
        return False
    elif game_board['a2'] == 'o' and game_board['b2'] == 'o' and game_board['c2'] == 'o':
        return False
    elif game_board['a3'] == 'x' and game_board['b3'] == 'x' and game_board['c3'] == 'x':
        return False
    elif game_board['a3'] == 'o' and game_board['b3'] == 'o' and game_board['c3'] == 'o':
        return False
    elif game_board['a1'] == 'x' and game_board['b2'] == 'x' and game_board['c3'] == 'x':
        return False
    elif game_board['a1'] == 'o' and game_board['b2'] == 'o' and game_board['c3'] == 'o':
        return False
    elif game_board['a3'] == 'x' and game_board['b2'] == 'x' and game_board['c1'] == 'x':
        return False
    elif game_board['a3'] == 'o' and game_board['b2'] == 'o' and game_board['c1'] == 'o':
        return False
    else:
        return True


still_playing = True
while still_playing:
    player = 'x'
    game_grid()
    gameround(player)
    still_playing = isthereawinner()
    player = 'o'
    game_grid()
    gameround(player)
    still_playing = isthereawinner()


print("we have a winner!")
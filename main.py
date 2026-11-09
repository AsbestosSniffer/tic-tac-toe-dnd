print("Welcome to Tic Tac Toe!")
print("This is a game for 2 users.\n" \
"You will each take turns specifying\n" \
"the coordinate of the box where you\n" \
"wish to place the X or O.\n" \
"X starts. Enjoy!") 

GAME_STATE = [['_' for _ in range(3)] for _ in range(3)]

def show_state():
    for r in GAME_STATE:
        for c in r: 
            print(c, end=' ')
        print()
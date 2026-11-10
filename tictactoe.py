import json
from enum import Enum

with open('error-codes.json') as error_file:
    error_json = error_file.read()

error_codes = json.loads(error_json)

class GameResult(Enum):
    DRAW = 0
    X_WINS = 1
    O_WINS = 2

BOARD_STATE = [['_' for _ in range(3)] for _ in range(3)]

# Counters to check for game end
# One-indexed for convenience
ROW_COUNTERS = [0, 0, 0, 0]
COL_COUNTERS = [0, 0, 0, 0]
DIAG_COUNTERS = [0, 0, 0]

def show_state():
    for r in BOARD_STATE:
        for c in r: 
            print(c, end=' ')
        print()
    print()

def validate_input(coords: str) -> bool:
    if len(coords) < 3:
        print(error_codes["TOO_SHORT"])
        return None 
    
    try:
        x = int(coords[0])
        y = int(coords[2])
    except ValueError:
        print(error_codes["NOT_INT"])
        return None 

    if x < 1 or x > 3 or y < 1 or y > 3:
        print(error_codes["NOT_IN_BOUNDS"])
        return None 

    if BOARD_STATE[x][y] != '_':
        print(error_codes["OCCUPIED"])
    return x, y
    
def prompt_user():
    print(
        "Input next mark position as comma-separated\n" \
        "row number and column number. The smallest\n" \
        "row/column number is 1, the largest is 3.\n" \
        "Examples: '1,3' or '2,2' are valid inputs.\n"
    )

    valid_input = None  
    while not valid_input:
        coords = input()
        valid_input = validate_input(coords)

    return valid_input 

def check_game_finish():
    pass


def handle_move(x, y):
    BOARD_STATE[x][y] = 'X' if X_turn else 'O'
    check_game_finish()

if __name__ == '__main__':
    print(
        "Welcome to Tic Tac Toe!\n" \
        "This is a game for 2 users.\n" \
        "You will each take turns specifying\n" \
        "the coordinate of the box where you\n" \
        "wish to place the X or O.\n" \
        "X starts. Enjoy!\n"
    ) 

    # if turn = True, it's X's turn
    # if turn = False, it's O's turn 
    X_turn = True 
    done = False
    while not done:
        show_state()
        validated_input = prompt_user() 
        handle_move(**validated_input)
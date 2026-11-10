import json
from enum import Enum
from itertools import chain 

with open('error-codes.json') as error_file:
    error_json = error_file.read()

error_codes = json.loads(error_json)

class GameStatus(Enum):
    DRAW = 0
    X_WINS = 1
    O_WINS = 2

board_state = [['_' for _ in range(3)] for _ in range(3)]

# Counters to check for game end
row_counters = [0, 0, 0]
col_counters = [0, 0, 0]
diag_counters = [0, 0]
total_num_moves = 0

def show_state():
    for r in board_state:
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

    if board_state[x-1][y-1] != '_':
        print(error_codes["OCCUPIED"])
        return None
    
    return x-1, y-1
    
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
    result = None 
    if any(x == 3 for x in chain(row_counters, col_counters, diag_counters)):
        result = GameStatus.X_WINS
    elif any(x == -3 for x in chain(row_counters, col_counters, diag_counters)):
        result = GameStatus.O_WINS
    elif total_num_moves >= 9:
        result = GameStatus.DRAW
    return result 


def handle_move(x, y):
    global total_num_moves 
    total_num_moves += 1
    board_state[x][y] = ('X' if X_turn else 'O')
    increment = 1 if X_turn else -1 
    row_counters[x] += increment
    col_counters[y] += increment
    if x == y:
        # first diagonal
        diag_counters[0] += increment 
    if x == 4 - y:
        # second diagonal 
        diag_counters[1] += increment         
    result = check_game_finish()
    return result 

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
        result = handle_move(*validated_input)
        X_turn = not X_turn
        if result:
            done = True 
            if result == GameStatus.X_WINS:
                print("X wins!")
            elif result == GameStatus.O_WINS:
                print("Y wins!")
            elif result == GameStatus.DRAW:
                print("Draw!")

import json

with open('error-codes.json') as error_file:
    error_json = error_file.read()

error_codes = json.loads(error_json)

GAME_STATE = [['_' for _ in range(3)] for _ in range(3)]

def show_state():
    for r in GAME_STATE:
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


if __name__ == '__main__':
    print(
        "Welcome to Tic Tac Toe!\n" \
        "This is a game for 2 users.\n" \
        "You will each take turns specifying\n" \
        "the coordinate of the box where you\n" \
        "wish to place the X or O.\n" \
        "X starts. Enjoy!\n"
    ) 

    done = False
    while not done:
        show_state()
        prompt_user() 
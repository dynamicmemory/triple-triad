def print_board(gameboard):
    print("+---+---+---+")
    print(f"| {gameboard[0][0][0]} | {gameboard[0][1][0]} | {gameboard[0][2][0]} |") 
    print(f"|{gameboard[0][0][3]} {gameboard[0][0][1]}|{gameboard[0][1][3]} {gameboard[0][1][1]}|{gameboard[0][2][3]} {gameboard[0][2][1]}|") 
    print(f"| {gameboard[0][0][2]} | {gameboard[0][1][2]} | {gameboard[0][2][2]} |") 
    print("+---+---+---+")
    print(f"| {gameboard[1][0][0]} | {gameboard[1][1][0]} | {gameboard[1][2][0]} |") 
    print(f"|{gameboard[1][0][3]} {gameboard[1][0][1]}|{gameboard[1][1][3]} {gameboard[1][1][1]}|{gameboard[1][2][3]} {gameboard[1][2][1]}|") 
    print(f"| {gameboard[1][0][2]} | {gameboard[1][1][2]} | {gameboard[1][2][2]} |") 
    print("+---+---+---+")
    print(f"| {gameboard[2][0][0]} | {gameboard[2][1][0]} | {gameboard[2][2][0]} |") 
    print(f"|{gameboard[2][0][3]} {gameboard[2][0][1]}|{gameboard[2][1][3]} {gameboard[2][1][1]}|{gameboard[2][2][3]} {gameboard[2][2][1]}|") 
    print(f"| {gameboard[2][0][2]} | {gameboard[2][1][2]} | {gameboard[2][2][2]} |") 
    print("+---+---+---+")

empty_squares: int = 9
p1_score: int = 5
p2_score: int = 5
default: dict = {"c1": [0,0,0,0], 
                 "c2": [0,0,0,0], 
                 "c3": [0,0,0,0], 
                 "c4": [0,0,0,0], 
                 "c5": [0,0,0,0], 
                 "c6": [0,0,0,0], 
                 "c7": [0,0,0,0], 
                 "c8": [0,0,0,0], 
                 "c9": [0,0,0,0]}

p1_hand: dict = {"c1": [1,2,3,4], 
                 "c2": [4,3,3,1], 
                 "c3": [3,1,1,1], 
                 "c4": [1,4,3,2], 
                 "c5": [1,1,1,4]}

p2_hand: dict = {"c1": [1,2,3,4], 
                 "c2": [4,3,3,1], 
                 "c3": [3,1,1,1], 
                 "c4": [1,4,3,2], 
                 "c5": [1,1,1,4]}

turn = "p1"
game_board = [[default["c1"], default["c2"], default["c3"]], 
              [default["c4"], default["c5"], default["c6"]], 
              [default["c4"], default["c5"], default["c6"]]]
legal_moves = []
while (empty_squares > 0):
    print_board(game_board)
    # Check the board to get all legal moves
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == [0,0,0,0]:
                legal_moves.append((row, col))

    print(legal_moves)

    row = input("Enter row to play ") 
    col = input("Enter col to play ") 

    print(p1_hand) 

    card = input("Enter card to play ") 
    
    game_board[int(row)][int(col)] = p1_hand[card]
    empty_squares -= 1

def place_card(card: list) -> None:
    print(f"| {card[0]} |")
    print(f"|{card[3]} {card[1]}|")
    print(f"| {card[2]} |")


def validate_move():
    pass 

# def legal_moves():
#     pass 



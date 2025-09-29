class Board:

    def __init__(self):
        self.height: int = 3
        self.width: int = 3
        self.board: list = self.generate_board()
        self.gameover: bool = False
        self.empty_tiles: int = 9


    def generate_board(self) -> list:
        """
        Creates a 2d array of 3x3 shape and fills each element with "empty"
        """
        board: list = [[],[],[]]
        for row in range(3):
            for col in range(3):
                board[row].append(None)
        return board


    def is_gameover(self) -> bool:
        """
        Returns True of False depending on if there are any tiles to play in
        """
        return True if self.empty_tiles == 0 else False


    def legal_moves(self) -> list:
        """
        Searches the board and finds all empty squares
        """
        moves: list = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == None:
                    moves.append((row, col))
        return moves

    
    def make_move(self, row: int, col: int, card) -> list:
        """
        Updates the board with the card played, decrements empty tiles and 
        calls flip_cards to mutate board state further depending on flips 
        """
        self.empty_tiles -= 1
        self.board[row][col] = card 
        return self.flip_cards(row, col)


    def flip_cards(self, row: int, col: int) -> list: 
        """ 
        Simple does too much, Flips cards if they can be flipped 
        """
        dirs = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
        played_card = self.board[row][col]
        flipped = []
        for key, val in dirs.items():
            row_off, col_off = val[0] + row, val[1] + col      
            if (row_off < 0 or row_off > 2) or (col_off < 0 or col_off > 2):
                continue 

            off_card = self.board[row_off][col_off]
            if off_card == None or off_card["player"] == played_card["player"]:
                continue 

            if key == "north":
                if played_card["north"] > off_card["south"]:
                    self.board[row_off][col_off]["player"] = played_card["player"]
                    self.board[row_off][col_off]["played"] = True
                    flipped.append((row_off, 
                                    col_off, 
                                    played_card["player"], 
                                    off_card["player"]))
            if key == "east":
                if played_card["east"] > off_card["west"]:
                    self.board[row_off][col_off]["player"] = played_card["player"]
                    self.board[row_off][col_off]["played"] = True
                    flipped.append((row_off, 
                                    col_off, 
                                    played_card["player"], 
                                    off_card["player"]))
            if key == "south":
                if played_card["south"] > off_card["north"]:
                    self.board[row_off][col_off]["player"] = played_card["player"]
                    self.board[row_off][col_off]["played"] = True
                    flipped.append((row_off, 
                                    col_off, 
                                    played_card["player"], 
                                    off_card["player"]))
            if key == "west":
                if played_card["west"] > off_card["east"]:
                    self.board[row_off][col_off]["player"] = played_card["player"]
                    self.board[row_off][col_off]["played"] = True
                    flipped.append((row_off, 
                                    col_off, 
                                    played_card["player"], 
                                    off_card["player"]))
        return flipped


    def test_print(self):
        return "It works"

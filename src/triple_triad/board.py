from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card

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
        for row in range(self.height):
            for col in range(self.width):
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
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == None:
                    moves.append((row, col))
        return moves

    
    def play_card(self, row: int, col: int, card: Card) -> list:
        """
        Updates the board with the card played, decrements empty tiles and 
        calls flip_cards to mutate board state further depending on flips 
        """
        self.empty_tiles -= 1
        self.board[row][col] = card 
        return self.flip_cards(row, col)


    def flip_cards(self, row: int, col: int) -> list: 
        """ 
        Checks all surrounding square of played card, flips any with lower score 
        to current players name
        Returns: List of all [(row, column, card of player, card that was flipped)]
        """
        dirs = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
        ops = {"north": "south", "east": "west", "south": "north", "west": "east"}
        played_card = self.board[row][col]
        flipped = []
        for key, val in dirs.items():
            row_off, col_off = val[0] + row, val[1] + col      
            # Eliminate coords that are off the board
            if (row_off < 0 or row_off > 2) or (col_off < 0 or col_off > 2):
                continue 

            # Eliminate empty squares
            off_card = self.board[row_off][col_off]
            if off_card == None or off_card["player"] == played_card["player"]:
                continue

            if played_card[key] > off_card[ops[key]]:
                off_card["player"] = played_card["player"]
                flipped.append((row_off, col_off, played_card["player"], off_card["player"]))

        return flipped


    def get_height(self) -> int:
        """ 
        Gets the gameboards height as an int
        """
        return self.height


    def get_width(self) -> int:
        """ 
        Gets the gameboards width as an int
        """
        return self.width


    def test_print(self):
        return "It works"

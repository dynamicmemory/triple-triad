from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from board import Board
    from player import Player
    from card import Card

class HumanAgent:

    def __init__(self):
        pass


    # def make_move(self, board: Board, player: Player) -> list:
    def make_move(self, board, row, col, card) -> list:
        """
        Makes a legal move on the game board and returns a list of coords, and cards flipped
        """
        # row, col = self.get_input_coords(board)
        # card: Card = self.get_input_card(player)
        
        return board.play_card(row, col, card)
        

    # TODO: Tighten this up, get rid of the try except
    def get_input_coords(self, board) -> tuple:
        """ 
        Gets the coordinates the user wants to play on the board. 
        """
        while (True):
            row = input("Enter the row you want to play on ")
            col = input("Enter the column you want to play on ")
            try:
                if (int(row), int(col)) in board.legal_moves():
                    return (int(row), int(col))
            except:
                print("You can only insert numbers from 1 to 3")


    # TODO: Fix if statement and card string
    def get_input_card(self, player: Player) -> Card:
        """ 
        Gets users card choice and returns the cards name 
        """ 
        while (True):
            card = input("Enter the card number you want to play ")
            card = f"card_{card}"
            player = player
            for c in player.get_unplayed_cards():
                if card == c["name"]:
                    player.set_played_card(card)
                    return player.get_card(card)
            print("You can only select card you have in your hand")

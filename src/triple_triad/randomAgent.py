import random as r
import copy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from card import Card
    from board import Board

class RandomAgent:

    def __init__(self):
        pass


    def make_move(self, board, player) -> list:
        """
        Plays a random card from hand at a random legal location on the board.
        """
        # Get all legal moves and randomly shuffle them
        legal_moves: list = board.legal_moves()
        r.shuffle(legal_moves)

        # Setup default vals for card, row and col 
        card: Card = None 
        row = col = 0

        # For all legal moves, check each unplayed card, simulate a turn, if that 
        # sim returns a list of atleast one flipped card, play that card.
        for move in legal_moves:
            flag: int = 0
            for card in player.get_unplayed_cards():
                temp_board: Board = copy.deepcopy(board)
                row, col = move
                score = temp_board.play_card(row, col, card)
                if len(score) > 0:
                    flag = 1
                    break
            if flag:
                break 

        # Gets the name of the card the AI played and sets it to used.
        card_name: str = card["name"]
        player.set_played_card(card_name)
        return board.play_card(row, col, card)




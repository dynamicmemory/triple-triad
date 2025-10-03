from triple_triad.board import Board
from triple_triad.player import Player
from triple_triad.randomAgent import RandomAgent
from triple_triad.humanAgent import HumanAgent

class Game:

    def __init__(self):
        self.board: Board = Board()
        self.players: list[Player] = self.create_players()
        self.turn: int = 0


    def create_players(self) -> list[Player]:
        """
        Creates two player objects for the game
        returns: List[p.Player]
        """
        p1: Player = Player("A", HumanAgent())
        p2: Player = Player("B", HumanAgent())
        return [p1, p2]


    def set_player_turn(self) -> None:
        """
        Sets the current players turn 
        """
        self.turn = 1 - self.turn
        self.players[self.turn] 


    def get_player_turn(self) -> Player:
        """
        Gets the current player
        """
        return self.players[self.turn]


    def update_scores(self, state: list) -> None: 
        """
        Updates both players scores depending on cards flipped on turn
        """
        self.get_player_turn().score += len(state) 
        self.players[1 - self.turn].score -= len(state) 


    def get_winner(self) -> str:
        """
        Determines winner of the game by comparing players scores.
        """
        if self.players[0].score > self.players[1].score:
            result = f"Player {self.players[0].name} is the Winner"
        elif self.players[1].score > self.players[0].score:
            result = f"Player {self.players[1].name} is the Winner"
        else:
            result = "Players tied."
        return result


    def get_board(self) -> Board:
        return self.board


    def print_player_hand(self):
        players_hand: list = self.get_player_turn().get_unplayed_cards()
        print("---Card scores---") 
        for card in players_hand:
            print(f"  {card["north"]}  |", end="")
        print()
        for card in players_hand:
            print(f" {card["west"]} {card["east"]} |", end="")
        print() 
        for card in players_hand:
            print(f"  {card["south"]}  |", end="")
        print()
        print("---Card Numbers---")
        for card in players_hand:
            print(f"  {card["name"][5]}  |", end="")
        print()


    def print_board(self):
        for row in range(self.board.height):
            print("+-----+-----+-----+")
            for inner_row in range(3):
                for col in range(self.board.width):
                    card = self.board.board[row][col]
                    if inner_row == 0:
                        if card is not None:
                            if col == 2:
                                print(f"|  {card["north"]}  |")
                            else:
                                print(f"|  {card["north"]}  ", end="")
                        else:
                            if col == 2:
                                print(f"|  0  |")
                            else:
                                print(f"|  0  ", end="")

                    if inner_row == 1:
                        if card is not None:
                            if col == 2:
                                print(f"|{card["west"]} {card["player"]} {card["east"]}|")
                            else:
                                print(f"|{card["west"]} {card["player"]} {card["east"]}", end="")
                        else:
                            if col == 2:
                                print(f"|0   0|")
                            else:
                                print(f"|0   0", end="")

                    if inner_row == 2:
                        if card is not None:
                            if col == 2:
                                print(f"|  {card["south"]}  |")
                            else:
                                print(f"|  {card["south"]}  ", end="")
                        else:
                            if col == 2:
                                print(f"|  0  |")
                            else:
                                print(f"|  0  ", end="")

        print("+-----+-----+-----+")
        print(f"Player A: {self.players[0].score}, Player B: {self.players[1].score}")


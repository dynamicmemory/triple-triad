import board as board
import player as p

class Game:

    def __init__(self):
        self.board: board.Board = board.Board()
        self.players: list[p.Player] = self.create_players()
        self.turn: int = 0


    def create_players(self) -> list[p.Player]:
        """
        Creates two player objects for the game
        returns: List[p.Player]
        """
        p1: p.Player = p.Player("A")
        p2: p.Player = p.Player("B")
        return [p1, p2]


    def set_player_turn(self) -> None:
        """
        Sets the current players turn 
        """
        self.turn = 1 - self.turn
        self.players[self.turn] 


    def get_player_turn(self) -> p.Player:
        """
        Gets the current player
        """
        return self.players[self.turn]


    # TODO: Tighten this up, get rid of the try except
    def get_input_coords(self) -> tuple:
        """ 
        Gets the coordinates the user wants to play on the board. 
        """
        while (True):
            row = input("Enter the row you want to play on ")
            col = input("Enter the column you want to play on ")
            try:
                if (int(row), int(col)) in self.board.legal_moves():
                    return (int(row), int(col))
            except:
                print("You can only insert numbers from 1 to 3")

    
    # TODO: Fix if statement and card string
    def get_input_card(self) -> p.card.Card:
        """ 
        Gets users card choice and returns the cards name 
        """ 
        while (True):
            card = input("Enter the card number you want to play ")
            card = f"card_{card}"
            player = self.get_player_turn()
            for c in player.get_unplayed_cards():
                if card == c["name"]:
                    return player.get_card(card)
                else:
                    print("You can only select card you have in your hand")


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
        winner = ""
        if self.players[0].score > self.players[1].score:
            winner = self.players[0].name 
        else:
            winner = self.players[1].name
        return winner


    def main_loop(self) -> None:
        """
        Main loop of the game 
        """ 
        while (not self.board.is_gameover()):
            # Print board and hand  
            self.print_board()
            self.print_player_hand()

            # Get input 
            row, col = self.get_input_coords()
            card = self.get_input_card()

            # Make move
            flipped_cards = self.board.make_move(row, col, card)
            self.update_scores(flipped_cards) 

            # Check terminal state 
            self.gameover = self.board.is_gameover()

            # switch turn 
            self.set_player_turn()

        self.print_board()
        print(f"Player {self.get_winner()} is the Winner")


    def print_player_hand(self):
        players_hand: list = self.get_player_turn().get_unplayed_cards()
        print("---Card scores---") 
        for card in players_hand:
            print(f"  {card["north"]}  |", end="")
        print()
        for card in players_hand:
            print(f" {card["east"]} {card["west"]} |", end="")
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
                                print(f"|{card["east"]} {card["player"]} {card["west"]}|")
                            else:
                                print(f"|{card["east"]} {card["player"]} {card["west"]}", end="")
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


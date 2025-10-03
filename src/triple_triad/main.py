from triple_triad.game import Game 
from triple_triad.player import Player 
from triple_triad.gui import GUI 

def main():

    # Create a game, print the board and the players hand 
    g: Game = Game()
    gui: GUI = GUI(g)
    # while (not g.board.is_gameover()):

        # gui.render_game()
        # g.print_board()
        # g.print_player_hand()

        # gui.event_loop()
        # Get the current players turn and call agent to prompt or execute move
        # player: Player = g.get_player_turn()
        # flipped_cards: list = player.agent.make_move(g.board, player)

        # Update the scores, check if the game is over, switch turns
        # g.update_scores(flipped_cards)
        # g.set_player_turn()

    # Once the last move has been made, print final board and announce winner 
    # g.print_board()
    # gui.render_game()
    # print(g.get_winner())

    input("")
    # gui.event_loop()


if __name__ == "__main__":
    main()

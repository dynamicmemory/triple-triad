from triple_triad.game import Game 
from triple_triad.player import Player 
from triple_triad.gui import GUI 

def main():
    # Create a game, print the board and the players hand 
    game: Game = Game()
    gui: GUI = GUI(game)
    state: str = "menu"
    while gui.running:
        game_board = game.get_board()
        if state == "menu":
            state = gui.draw_menu()

        elif state == "game":
            gui.render_game()

            # AI players call its make move directly and update state (change?) 
            if game.get_player_turn().ai:
                player: Player = game.get_player_turn()
                flipped_cards: list = player.get_agent().make_move(game_board, player)
                game.update_scores(flipped_cards)
                game.set_player_turn()

            # Human players enters the event loop, game will listen for clicks
            gui.event_loop()
            gui.clock.tick(60)
            if game_board.is_gameover():
                state = "gameover"
                # Render last move then leave to gameover screen
                gui.render_game()

        elif state == "gameover":
            state = gui.draw_gameover(game.get_winner())

        elif state == "quit":
            break

if __name__ == "__main__":
    main()

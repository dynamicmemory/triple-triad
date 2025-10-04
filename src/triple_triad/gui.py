# TODO: Refactor the whole class once gui logic and event loop fully working.
from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
    from game import Game
    from board import Board
    from player import Player
    from card import Card

# Colour scheme for the game 
white: tuple = (225, 225, 225)
black: tuple = (0, 0, 0)
orange: tuple = (220, 130, 0)
green: tuple = (200, 225, 0)
bulma: tuple = (0, 220, 130)
trunks: tuple = (0, 200, 220)
purple: tuple = (130, 0, 220)
blue: tuple = (0, 90, 220)

class GUI:

    def __init__(self, game: Game):
        pygame.init()
        pygame.display.set_caption("Triple Triad")

        self.game: Game = game
        self.screen = pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.running: bool = True
        self.is_card_clicked: bool = False 
        self.selected_card: None|Card = None
        self.hand_clicked: dict = {}
        self.board_clicked: dict = {}
        self.game_event_map: dict = {"board": self.board_clicked, "hands": self.hand_clicked}


    def event_loop(self) -> None:
        curr_player: Player = self.game.get_player_turn()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Selects the card that was clicked
                for (player, card), rect in self.game_event_map["hands"].items():
                    if (rect != None and rect.collidepoint(event.pos) and curr_player == player):
                        self.selected_card = curr_player.get_card(card)
                        self.is_card_clicked = True

                # Selects the place on the board to put the card 
                for (row, col), rect in self.game_event_map["board"].items():
                    if (rect.collidepoint(event.pos) and self.is_card_clicked and 
                        self.game.board.board[row][col] == None):
                        flipped: list = curr_player.agent.make_move(self.game.board, 
                                                              row, col, self.selected_card) 

                        # Cleans up all the details after a player plays a card 
                        curr_player.set_played_card(self.selected_card["name"])
                        self.hand_clicked[(curr_player, self.selected_card["name"])] = None
                        self.is_card_clicked = False 
                        self.selected_card = None
                        self.game.update_scores(flipped)
                        self.game.set_player_turn()


    # TODO: Correctly math out all rendering using relative sizes
    def render_game(self):
        board: Board = self.game.get_board()
        # Draw the gameboard and hand area backgounds
        pygame.draw.rect(self.screen, orange, (250, 10, 400, 580))
        pygame.draw.rect(self.screen, bulma, (25, 10, 200, 580))   #p1 hand area
        pygame.draw.rect(self.screen, green, (675, 10, 200, 580))  #p2 hand area

        # Draw the 9 cards on the gameboard
        height: int = 20 
        gap_offset: int = 15
        card_width: int = 100 
        card_height: int = 175
        for row in range(board.get_height()):
            width: int = 285
            for col in range(board.get_width()):

                # Get value at board location
                card: Card = self.game.get_board().board[row][col]

                # if a card exists at location, paints scores and player colour 
                if card:
                    colour: tuple = purple if card["player"] == "A" else trunks
                    font_colour: tuple = white if card["player"] == "A" else black
                    rect = pygame.draw.rect(self.screen, colour, (width, height, 
                                                                  card_width, 
                                                                  card_height))

                    # TODO: Redo these calcs better and more efficent and relative
                    font = pygame.font.Font(None, 60)
                    north = font.render(f"{card["north"]}", True, font_colour)
                    east = font.render(f"{card["east"]}", True, font_colour)
                    south = font.render(f"{card["south"]}", True, font_colour)
                    west = font.render(f"{card["west"]}", True, font_colour)
                    self.screen.blit(north, (325 + (col * (card_width + gap_offset)), 
                                             25 + (row * (card_height + gap_offset))))
                    self.screen.blit(east, (355 + (col * (card_width + gap_offset)), 
                                            90 + (row * (card_height+gap_offset))))
                    self.screen.blit(south, (325 + (col * (card_width + gap_offset)), 
                                             155 + (row * (card_height + gap_offset))))
                    self.screen.blit(west, (295 + (col * (card_width + gap_offset)), 
                                            90 + (row * (card_height + gap_offset))))

                else: 
                    rect = pygame.draw.rect(self.screen, white, (width, height, 
                                                                 card_width, 
                                                                 card_height))

                # Stores the click on the gameboard made by the player 
                self.board_clicked[(row, col)] = rect

                # Draw the card border
                pygame.draw.rect(self.screen, black, (width, height, 
                                                      card_width, card_height), 2)

                # Add one card width per col 
                width += card_width + gap_offset
            # Add one card heigh per row
            height += card_height + gap_offset     # This should be done better

        # Draw hands 
        p1: int = 75     # Where to start drawing p1s cards
        p2: int = 725    # Where to start drawing p2s cards (clean these up) 
        height: int = 20
        for num in range(5):
            card: Card = self.game.players[0].get_card(f"card_{num}")
            if not card["played"]:
                rect = pygame.draw.rect(self.screen, purple, (p1, height, card_width, card_height))
                pygame.draw.rect(self.screen, black, (p1, height, card_width, card_height), 2)
                self.hand_clicked[(self.game.players[0], f"card_{num}")] = rect
                # Draw the cards scores on the card
                font = pygame.font.Font(None, 30)
                north = font.render(f"{card["north"]}", True, white)
                east = font.render(f"{card["east"]}", True, white)
                south = font.render(f"{card["south"]}", True, white)
                west = font.render(f"{card["west"]}", True, white)
                self.screen.blit(north, (120, 30+(num * (card_height/2))))
                self.screen.blit(east, (140, 55+(num * (card_height/2))))
                self.screen.blit(south, (120, 80+(num * (card_height/2))))
                self.screen.blit(west, (100, 55+(num * (card_height/2))))

            card = self.game.players[1].get_card(f"card_{num}")
            if not card["played"]:
                rect = pygame.draw.rect(self.screen, trunks, (p2, height, card_width, card_height))
                pygame.draw.rect(self.screen, black, (p2, height, card_width, card_height), 2)
                self.hand_clicked[(self.game.players[1], f"card_{num}")] = rect

                # Draw the cards scores on the card
                font = pygame.font.Font(None, 30)
                north = font.render(f"{card["north"]}", True, black)
                east = font.render(f"{card["east"]}", True, black)
                south = font.render(f"{card["south"]}", True, black)
                west = font.render(f"{card["west"]}", True, black)
                self.screen.blit(north, (770, 30+(num * (card_height/2))))
                self.screen.blit(east, (790, 55+(num * (card_height/2))))
                self.screen.blit(south, (770, 80+(num * (card_height/2))))
                self.screen.blit(west, (750, 55+(num * (card_height/2))))   

            height += int(card_height / 2)
       
        self.draw_score()
        pygame.display.update()


    # TODO: Loop through players instead of duplicating calls
    def draw_score(self):
        """
        Draws the score for both players on the game board
        """
        font = pygame.font.Font(None, 60)
        p1_score = font.render(f"{self.game.players[0].score}", True, black)
        p2_score = font.render(f"{self.game.players[1].score}", True, black)
        self.screen.blit(p1_score, (125, 550))
        self.screen.blit(p2_score, (775, 550))


    # TODO: Break this up into smaller functions once all menus are fin
    # TODO: Turn all buttons and text into dict to iterate over once for gen
    def draw_menu(self):
        # Set default backgournd and font for menu
        pygame.draw.rect(self.screen, black, (0, 0, 900, 600))
        font = pygame.font.Font(None, 40)

        singleplayer = pygame.draw.rect(self.screen, trunks, (350, 100, 200, 50))
        single_text = font.render("Single player", True, black)
        self.screen.blit(single_text, (360, 110))

        multplayer = pygame.draw.rect(self.screen, trunks, (350, 200, 200, 50))
        multi_text = font.render("Multiplayer", True, black)
        self.screen.blit(multi_text, (380, 210))

        quit = pygame.draw.rect(self.screen, orange, (350, 300, 200, 50))
        quit_text = font.render("Quit", True, black)
        self.screen.blit(quit_text, (420, 310))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayer.collidepoint(event.pos): 
                    self.game.setup_players("human", "ai")
                    # Set up ai on human
                    return "game"
                elif multplayer.collidepoint(event.pos):
                    self.game.setup_players("human", "human")
                    # Set up human on human
                    return "game"
                elif quit.collidepoint(event.pos):
                    pygame.quit()
                    return "quit"

        pygame.display.update()
        return "menu"


    def draw_gameover(self, winner_message: str):
        # Set default backgournd and font for menu
        pygame.draw.rect(self.screen, bulma, (270, 50, 350, 500))
        font = pygame.font.Font(None, 40)
        
        winner_text = font.render(f"{winner_message}", True, black)
        self.screen.blit(winner_text, (360, 110))

        rematch = pygame.draw.rect(self.screen, trunks, (350, 200, 200, 50))
        rematch_text = font.render("Rematch", True, black)
        self.screen.blit(rematch_text, (390, 210))

        menu = pygame.draw.rect(self.screen, trunks, (350, 300, 200, 50))
        menu_text = font.render("Back to Menu", True, black)
        self.screen.blit(menu_text, (360, 310))

        quit = pygame.draw.rect(self.screen, orange, (350, 400, 200, 50))
        quit_text = font.render("Quit", True, black)
        self.screen.blit(quit_text, (420, 410))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rematch.collidepoint(event.pos): 
                    self.game.reset_game()
                    return "game"

                elif menu.collidepoint(event.pos):
                    self.game.reset_game()
                    return "menu"

                elif quit.collidepoint(event.pos):
                    pygame.quit()
                    return "quit"

        pygame.display.update()
        return "gameover"


    def draw_board(self):
        pass

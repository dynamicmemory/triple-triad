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
        player: Player = self.game.get_player_turn()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Selects the card that was clicked
                for (p, c), rect in self.game_event_map["hands"].items():
                    if (rect != None and rect.collidepoint(event.pos) and player == p):
                        self.selected_card = player.get_card(c)
                        self.is_card_clicked = True

                # Selects the place on the board to put the card 
                for (row, col), rect in self.game_event_map["board"].items():
                    if (rect.collidepoint(event.pos) and self.is_card_clicked and 
                        self.game.get_board().board[row][col] == None):
                        flip: list = player.get_agent().make_move(self.game.get_board(), 
                                                              row, col, self.selected_card) 

                        # Cleans up all the details after a player plays a card 
                        player.set_played_card(self.selected_card["name"])
                        self.hand_clicked[(player, self.selected_card["name"])] = None
                        self.is_card_clicked = False 
                        self.selected_card = None
                        self.game.update_scores(flip)
                        self.game.set_player_turn()


    def render_game(self):
        self.draw_board()
        self.draw_hands()
        self.draw_score()
        pygame.display.update()


    # TODO: Correctly math out all rendering using relative sizes
    def draw_board(self):    
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
                card_coords = (width, height, card_width, card_height)
                col_off = col * (card_width + gap_offset)  
                row_off = row * (card_height + gap_offset)  

                # Set a card to blank
                rect = pygame.draw.rect(self.screen, white, card_coords)

                # Get value at board location
                card: Card = self.game.get_board().board[row][col]

                # if a card exists at location, paints scores and player colour 
                if card:
                    colour: tuple = purple if card["player"] == "A" else trunks
                    font_colour: tuple = white if card["player"] == "A" else black
                    rect = pygame.draw.rect(self.screen, colour, card_coords)

                    self.draw_text(f"{card["north"]}", font_colour, 60, (325+col_off, 25+row_off))
                    self.draw_text(f"{card["east"]}", font_colour, 60, (355+col_off, 90+row_off))
                    self.draw_text(f"{card["south"]}", font_colour, 60, (325+col_off, 155+row_off))
                    self.draw_text(f"{card["west"]}", font_colour, 60, (295+col_off, 90+row_off))

                # Stores the click on the gameboard made by the player 
                self.board_clicked[(row, col)] = rect

                # Draw the card border
                pygame.draw.rect(self.screen, black, card_coords, 2)

                # Add one card width per col 
                width += card_width + gap_offset
            # Add one card heigh per row
            height += card_height + gap_offset     # This should be done better


    def draw_hands(self):
        p1: int = 75     # Where to start drawing p1s cards
        p2: int = 725    # Where to start drawing p2s cards (clean these up) 
        height: int = 20
        card_width: int = 100 
        card_height: int = 175
        for num in range(5):
            off_set = num * (card_height/2)

            card: Card = self.game.players[0].get_card(f"card_{num}")
            if not card["played"]:
                rect = pygame.draw.rect(self.screen, purple, (p1, height, card_width, card_height))
                pygame.draw.rect(self.screen, black, (p1, height, card_width, card_height), 2)

                # Saves clicked card to map
                self.hand_clicked[(self.game.players[0], f"card_{num}")] = rect

                # Draw the cards scores on the card
                self.draw_text(f"{card["north"]}", white, 30,(120, 30 + off_set))
                self.draw_text(f"{card["east"]}", white, 30, (140, 55 + off_set))
                self.draw_text(f"{card["south"]}", white, 30,(120, 80 + off_set)) 
                self.draw_text(f"{card["west"]}", white, 30,(100, 55 + off_set)) 

            card = self.game.players[1].get_card(f"card_{num}")
            if not card["played"]:
                rect = pygame.draw.rect(self.screen, trunks, (p2, height, card_width, card_height))
                pygame.draw.rect(self.screen, black, (p2, height, card_width, card_height), 2)

                # Saves clicked card to map
                self.hand_clicked[(self.game.players[1], f"card_{num}")] = rect

                # Draw the cards scores on the card
                self.draw_text(f"{card["north"]}", black, 30,(770, 30 + off_set))
                self.draw_text(f"{card["east"]}", black, 30,(790, 55 + off_set))
                self.draw_text(f"{card["south"]}", black, 30,(770, 80 + off_set)) 
                self.draw_text(f"{card["west"]}", black, 30,(750, 55 + off_set)) 

            height += int(card_height / 2)


    def draw_text(self, text, t_col, font_size, t_coords):
        font = pygame.font.Font(None, font_size)
        t = font.render(f"{text}", True, t_col)
        self.screen.blit(t, t_coords)


    def draw_score(self):
        """
        Draws the score for both players on the game board
        """
        font = pygame.font.Font(None, 60)
        players = [(self.game.players[0],125),(self.game.players[1],775)]
        for player in players:
            score = font.render(f"{player[0].score}", True, black)
            self.screen.blit(score, (player[1], 550))


    # TODO: Break this up into smaller functions once all menus are fin
    # TODO: Turn all buttons and text into dict to iterate over once for gen
    def draw_menu(self):
        # Set default backgournd and font for menu
        pygame.draw.rect(self.screen, black, (0, 0, 900, 600))
        s = self.menu_helper(trunks, (350, 100, 200, 50), "Single Player", (360, 110))
        m = self.menu_helper(trunks, (350, 200, 200, 50), "Multiplayer", (380, 210))
        q = self.menu_helper(orange, (350, 300, 200, 50), "Quit", (420, 310))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if s.collidepoint(event.pos): 
                    self.game.setup_players("human", "ai")
                    return "game"
                elif m.collidepoint(event.pos):
                    self.game.setup_players("human", "human")
                    return "game"
                elif q.collidepoint(event.pos):
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

        rematch = self.menu_helper(trunks, (350, 200, 200, 50), "Rematch", (390,210))
        menu = self.menu_helper(trunks, (350, 300, 200, 50), "Back To Menu", (360,310))
        quit_game = self.menu_helper(orange, (350, 400, 200, 50), "Quit", (420,410))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rematch.collidepoint(event.pos): 
                    self.game.reset_game()
                    return "game"

                elif menu.collidepoint(event.pos):
                    self.game.reset_game()
                    return "menu"

                elif quit_game.collidepoint(event.pos):
                    pygame.quit()
                    return "quit"

        pygame.display.update()
        return "gameover"


    def menu_helper(self, colour, rect_coords, text, text_cords):
        """
        Draws text and panels for menus and returns the panels
        """
        button = pygame.draw.rect(self.screen, colour, rect_coords) 
        t = pygame.font.Font(None, 40).render(f"{text}", True, black) 
        self.screen.blit(t, text_cords) 
        return button 

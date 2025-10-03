from __future__ import annotations
from typing import TYPE_CHECKING
import pygame 

if TYPE_CHECKING:
    from game import Game
    from board import Board

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
        self.game = game

        pygame.init()
        pygame.display.set_caption("Triple Triad")
        self.screen = pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.is_card_clicked = False 
        self.card_clicked = None
        self.hand_clicked = {}
        self.board_clicked = {}
        self.game_event_map = {"board": self.board_clicked,
                               "hands": self.hand_clicked
                               }
        self.event_loop()

    def event_loop(self): 
        while not self.game.board.is_gameover() and self.running:
            self.render_game()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False 

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for (player, card), rect in self.game_event_map["hands"].items():
                        if (rect != None and rect.collidepoint(event.pos) and 
                            self.game.get_player_turn() == player):
                            self.card_clicked = self.game.get_player_turn().get_card(card)
                            self.is_card_clicked = True
                            # DONT FORGET - to remove the card from the map
                            print(f"Clicked {player}'s card: {card}")


                            print(self.is_card_clicked, self.card_clicked)
                    for (row, col), rect in self.game_event_map["board"].items():
                        if (rect.collidepoint(event.pos) and self.is_card_clicked and 
                            self.game.board.board[row][col] == None):
                            print(f"Clicked board at {row, col}")
                            flipped = self.game.get_player_turn().agent.make_move(self.game.board, 
                                                                        row, col, self.card_clicked) 

                            self.game.get_player_turn().set_played_card(self.card_clicked["name"])
                            self.hand_clicked[(self.game.get_player_turn(), self.card_clicked["name"])] = None
                            self.is_card_clicked = False 
                            self.card_clicked = None
                            self.game.update_scores(flipped)
                            self.game.set_player_turn()
                            


            self.clock.tick(60)
        self.render_game()
        print(f"The winner is {self.game.get_winner()}")


    # TODO: Correctly math out all rendering using relative sizes
    def render_game(self):
        board: Board = self.game.get_board()
        # Draw the gameboard and hand area backgounds
        pygame.draw.rect(self.screen, orange, (250, 10, 400, 580))
        pygame.draw.rect(self.screen, bulma, (25, 10, 200, 580))
        pygame.draw.rect(self.screen, green, (675, 10, 200, 580))

        # Draw the 9 cards on the gameboard
        height = 20 
        gap_offset = 15
        card_width = 100 
        card_height = 175
        for row in range(board.get_height()):
            width = 285
            for col in range(board.get_width()):

                # Get value at board location
                card = self.game.get_board().board[row][col]

                # if a card exists at location, paints scores and player colour 
                if card:
                    colour = purple if card["player"] == "A" else trunks
                    font_colour = white if card["player"] == "A" else black
                    rect = pygame.draw.rect(self.screen, colour, (width, height, card_width, card_height))
                    self.board_clicked[(row, col)] = rect

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
                    rect = pygame.draw.rect(self.screen, white, (width, height, card_width, card_height))
                    self.board_clicked[(row, col)] = rect

                # Draw the card border
                pygame.draw.rect(self.screen, black, (width, height, card_width, card_height), 2)

                
                width += card_width + gap_offset
            height += card_height + gap_offset# This should be done better

        # Draw hands 
        p1: int = 75     # Where to start drawing p1s cards
        p2: int = 725    # Where to start drawing p2s cards (clean these up) 
        height: int = 20
        for num in range(5):
            card = self.game.players[0].get_card(f"card_{num}")
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
       
        # Draw score
        font = pygame.font.Font(None, 60)
        p1_score = font.render(f"{self.game.players[0].score}", True, black)
        p2_score = font.render(f"{self.game.players[1].score}", True, black)
        self.screen.blit(p1_score, (125, 550))
        self.screen.blit(p2_score, (775, 550))

        pygame.display.update()

        # pygame.draw.rect(self.screen, (200, 225, 0), (100, 100, 100, 100))
        # pygame.display.update()
        pass

    def draw_board(self):
        pass

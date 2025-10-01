import unittest 
from triple_triad.board import Board
from triple_triad.game import Game
from triple_triad.player import Player
from triple_triad.card import Card

class TestBoard(unittest.TestCase): 

    def test_creates_board_test(self):
        self.assertEqual(Board().test_print(), "It works", "Board was created")


    def test_creates_board(self):
        self.assertEqual(Board().board[2][2], None, "Board should inialize empty squares")
        self.assertEqual(len(Board().board), 3, "Board should inialize 3 rows")
        self.assertEqual(len(Board().board[0]), 3, "Board should inialize 3 columns")


    def test_legal_moves(self):
        test_board = [["test", None, "test"],
                      ["test", None, None],
                      ["test", "test", None]]
        b = Board()
        b.board = test_board
        self.assertEqual(b.legal_moves(), [(0,1),(1,1),(1,2),(2,2)], "The board should have 4 empty tiles")


    # Player tests
    def test_creates_two_players(self):
        game = Game()
        players = game.create_players()

        self.assertEqual(len(players), 2, 
                         "A Game must create only two players")
        
        # Testing if set_player_turn() correctly switches the players turn
        self.assertEqual(game.get_player_turn().name, players[0].name)
        game.set_player_turn() 
        self.assertEqual(game.get_player_turn().name, players[1].name)


    def test_flip_card(self):
        # Create two cards to test for flipping 
        def_card = Card("A", 0).generate_card()
        def_card["south"] = 1

        atk_card = Card("B", 0).generate_card()
        atk_card["north"] = 2

        test_board = [[def_card, None, None],
                      [None, None, None],
                      [None, None, None]]

        board = Board()
        board.board = test_board
        board.make_move(0, 0, def_card)
        
        self.assertEqual(board.board[0][0], def_card, "Square should equal def_card")
        self.assertEqual(board.empty_tiles, 8, "There should be 8 empty tiles")
        
        # Test that playing a card that can flip, does flip
        board.make_move(1, 0, atk_card)
        self.assertEqual(board.board[1][0], atk_card, "Square should equal atk_card")
        self.assertEqual(board.board[0][0]["player"], "B", "Square should equal atk_card")

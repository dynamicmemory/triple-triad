import unittest 
from triple_triad.game import Game as game
from triple_triad.board import Board as board
from triple_triad.player import Player as player

# class TestBoard(unittest.TestCase): 
#
    # Board tests
    # def test_creates_board_test(self):
    #     b = board()
        # self.assertEqual(b.test_print(), "It works", "Board was created")


    # def test_creates_board(self):
    #     self.assertEqual(board.Board().board[2][2], None, "Board should inialize empty squares")
    #     self.assertEqual(len(board.Board().board), 3, "Board should inialize 3 rows")
    #     self.assertEqual(len(board.Board().board[0]), 3, "Board should inialize 3 columns")
    #
    #
    # def test_legal_moves(self):
    #     test_board = [["test", None, "test"],
    #                   ["test", None, None],
    #                   ["test", "test", None]]
    #     b = board.Board()
    #     b.board = test_board
    #     self.assertEqual(b.legal_moves(), [(0,1),(1,1),(1,2),(2,2)], "The board should have 4 empty tiles")
    #
    #
    # # Player tests
    # def test_creates_two_players(self):
    #     self.assertEqual(len(game.Game().create_players()), 2, 
    #                      "A Game must create only two players")



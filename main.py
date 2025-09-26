import game as game 


def main():
   game.setup()  


if __name__ == "__main__":
    main()




# def print_board(gameboard):
#     print("+---+---+---+")
#     print(f"| {gameboard[0][0][0]} | {gameboard[0][1][0]} | {gameboard[0][2][0]} |") 
#     print(f"|{gameboard[0][0][3]}{gameboard[0][0][4]}{gameboard[0][0][1]}|{gameboard[0][1][3]}{gameboard[0][1][4]}{gameboard[0][1][1]}|{gameboard[0][2][3]}{gameboard[0][2][4]}{gameboard[0][2][1]}|") 
#     print(f"| {gameboard[0][0][2]} | {gameboard[0][1][2]} | {gameboard[0][2][2]} |") 
#     print("+---+---+---+")
#     print(f"| {gameboard[1][0][0]} | {gameboard[1][1][0]} | {gameboard[1][2][0]} |") 
#     print(f"|{gameboard[1][0][3]}{gameboard[1][0][4]}{gameboard[1][0][1]}|{gameboard[1][1][3]}{gameboard[1][1][4]}{gameboard[1][1][1]}|{gameboard[1][2][3]}{gameboard[1][2][4]}{gameboard[1][2][1]}|") 
#     print(f"| {gameboard[1][0][2]} | {gameboard[1][1][2]} | {gameboard[1][2][2]} |") 
#     print("+---+---+---+")
#     print(f"| {gameboard[2][0][0]} | {gameboard[2][1][0]} | {gameboard[2][2][0]} |") 
#     print(f"|{gameboard[2][0][3]}{gameboard[2][0][4]}{gameboard[2][0][1]}|{gameboard[2][1][3]}{gameboard[2][1][4]}{gameboard[2][1][1]}|{gameboard[2][2][3]}{gameboard[2][2][4]}{gameboard[2][2][1]}|") 
#     print(f"| {gameboard[2][0][2]} | {gameboard[2][1][2]} | {gameboard[2][2][2]} |") 
#     print("+---+---+---+")
#
# empty_squares: int = 9
# p1_score: int = 5
# p2_score: int = 5
# default: dict = {"c1": [0,0,0,0,"N"], 
#                  "c2": [0,0,0,0,"N"], 
#                  "c3": [0,0,0,0,"N"], 
#                  "c4": [0,0,0,0,"N"], 
#                  "c5": [0,0,0,0,"N"], 
#                  "c6": [0,0,0,0,"N"], 
#                  "c7": [0,0,0,0,"N"], 
#                  "c8": [0,0,0,0,"N"], 
#                  "c9": [0,0,0,0,"N"]}
#
# p1_hand: dict = {"c1": [1,2,3,4,"A","U"], 
#                  "c2": [4,3,3,1,"A","U"], 
#                  "c3": [3,1,1,1,"A","U"], 
#                  "c4": [1,4,3,2,"A","U"], 
#                  "c5": [1,1,1,4,"A","U"]}
#
# p2_hand: dict = {"c1": [1,2,3,4,"B","U"], 
#                  "c2": [4,3,3,1,"B","U"], 
#                  "c3": [3,1,1,1,"B","U"],
#                  "c4": [1,4,3,2,"B","U"], 
#                  "c5": [1,1,1,4,"B","U"]}
#
# player_turn = "A"
# player_hand = p1_hand
# game_board = [[default["c1"], default["c2"], default["c3"]], 
#               [default["c4"], default["c5"], default["c6"]], 
#               [default["c7"], default["c8"], default["c9"]]]
# legal_moves = []
#
# while (empty_squares > 0):
#     flipped = 0
#     # Print the players turn and game board
#     print(f"Player {player_turn} turn")
#     print_board(game_board)
#
#     # Check the board to get all legal moves
#     for row in range(len(game_board)):
#         for col in range(len(game_board[row])):
#             if game_board[row][col] == [0,0,0,0,"N"]:
#                 legal_moves.append((row, col))
#
#     # Populate the legal moves list 
#     print(f"Legal Moves: {legal_moves}")
#     for key, val in player_hand.items():
#         print(key, val)
#
#     # Enter where to play and what to play
#     row = col = 9
#     while True:
#         row = input("Enter row to play ") 
#         col = input("Enter col to play ") 
#         if (int(row), int(col)) in legal_moves:
#             break 
#         print("Move is illegal, try again")
#
#     while True:
#         card = input("Enter card to play ") 
#         if card not in ["c1","c2","c3","c4","c5"]:
#             print("Not a card in your hand")
#             continue
#
#         if player_hand[card][5] == "U":
#             player_hand[card][5] = "P"
#             break 
#         print("Card has already been played")
#
#     opponent_turn = "A" if player_turn == "B" else "B"
#     empty_squares -= 1
#
#     offsets = [(-1,0,"north"),(0,1,"east"),(1,0,"south"),(0,-1,"west")]
#
#     potential_flips = []
#     attacking_edges = []
#     for off in offsets:
#         row_offset, col_offset = int(row) + off[0], int(col) + off[1]
#         try: 
#             potential_flip = game_board[row_offset][col_offset]  
#             if potential_flip[4] == player_turn:
#                 continue
#
#             if potential_flip[4] == "N":
#                 continue 
#
#             potential_flips.append((potential_flip, off[2]))
#             print(f"potential flips {potential_flip}")
#         except:
#             continue
#
#     for off in offsets:
#         row_offset, col_offset = int(row) + off[0], int(col) + off[1]
#         if (0 > row_offset or row_offset > 2) or (0 > col_offset or col_offset > 2):
#             continue
#
#         attacking_edges.append(off[2])
#         print(f"attacking_edge {off[2]}")
#
#     # Changing the 
#     game_board[int(row)][int(col)] = player_hand[card]
#
#     for edge in attacking_edges:
#         for flip in potential_flips:
#             if edge == "north" and flip[1] == "north":
#                 print(f"Edge {edge} flip {flip[1]}")
#                 print(f"game_board {game_board[int(row)][int(col)][0]} flipval {flip[0][2]}")
#                 if game_board[int(row)][int(col)][0] > flip[0][2]:
#
#                     flipped = 1
#                     # flip[0][4] = player_turn
#                     game_board[int(row) + offsets[0][0]][int(col) + offsets[0][1]][4] = player_turn
#                     if player_turn == "A":
#                         p1_score += 1
#                         p2_score -= 1 
#                     else: 
#                         p1_score -= 1
#                         p2_score += 1 
#             if edge == "east" and flip[1] == "east":
#                 if game_board[int(row)][int(col)][1] > flip[0][3]:
#                     flipped = 1
#                     # flip[0][4] = player_turn
#                     game_board[int(row) + offsets[1][0]][int(col) + offsets[1][1]][4] = player_turn
#                     if player_turn == "A":
#                         p1_score += 1
#                         p2_score -= 1 
#                     else: 
#                         p1_score -= 1
#                         p2_score += 1 
#             if edge == "south" and flip[1] == "south":
#                 if game_board[int(row)][int(col)][2] > flip[0][0]:
#                     flipped = 1
#                     # flip[0][4] = player_turn
#                     game_board[int(row) + offsets[2][0]][int(col) + offsets[2][1]][4] = player_turn
#                     if player_turn == "A":
#                         p1_score += 1
#                         p2_score -= 1 
#                     else: 
#                         p1_score -= 1
#                         p2_score += 1 
#             if edge == "west" and flip[1] == "west":
#                 if game_board[int(row)][int(col)][3] > flip[0][1]:
#                     flipped = 1
#                     game_board[int(row) + offsets[3][0]][int(col) + offsets[3][1]][4] = player_turn
#                     # flip[0][4] = player_turn
#                     if player_turn == "A":
#                         p1_score += 1
#                         p2_score -= 1 
#                     else: 
#                         p1_score -= 1
#                         p2_score += 1 
#
#     # if flipped == 0:
#     #     game_board[int(row)][int(col)] = player_hand[card]
#
#     player_hand = p1_hand if player_hand == p2_hand else p2_hand
#     player_turn = "A" if player_turn == "B" else "B"
#     legal_moves = []
#     print(f"Player 1 score {p1_score} Player 2 score {p2_score}")
#
# winner = "A" if p1_score > p2_score else "B"
#
# print(f"Player A score {p1_score} \nPlayer B score {p2_score}\nPlayer {winner} is the winner") 

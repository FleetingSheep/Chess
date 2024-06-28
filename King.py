import numpy
from Piece import Piece, get_selected

class King(Piece): #inherits the piece class
    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = []
        
        if self.has_moved == False: #castling

            try:
                if pieces[f"{self.color}r1"].has_moved == False: #castling to the left
                    if board[self.y, (self.x - 1)] == '0' and board[self.y, (self.x - 2)] == '0': #if space uninterrupted

                        if self.color == "b":
                            if board[self.y, (self.x - 1)] not in white_moves and board[self.y, (self.x - 2)] not in white_moves and board[self.y, (self.x - 3)] not in white_moves: #if not moving through check
                               self.moves.append([self.y, (self.x - 2)])

                        else:
                            if board[self.y, (self.x - 1)] not in black_moves and board[self.y, (self.x - 2)] not in black_moves and board[self.y, (self.x - 3)] not in black_moves: #if not moving through check
                                self.moves.append([self.y, (self.x - 2)])


                if pieces[f"{self.color}r2"].has_moved == False: #castling to the right
                    if board[self.y, (self.x + 1)] == '0' and board[self.y, (self.x + 2)] == '0': #if space uninterrupted

                        if self.color == "b":
                            if board[self.y, (self.x + 1)] not in white_moves and board[self.y, (self.x + 2)] not in white_moves: #if not moving through check
                               self.moves.append([self.y, (self.x + 2)])

                        else:
                            if board[self.y, (self.x + 1)] not in black_moves and board[self.y, (self.x + 2)] not in black_moves: #if not moving through check
                                self.moves.append([self.y, (self.x + 2)])

            except:
                pass
        
        self.moves.append([(self.y + 1), (self.x)]) #move down
        self.moves.append([(self.y - 1), (self.x)]) #move up
        self.moves.append([(self.y), (self.x - 1)]) #move left
        self.moves.append([(self.y), (self.x + 1)]) #move right
        self.moves.append([(self.y - 1), (self.x - 1)]) #move top left
        self.moves.append([(self.y - 1), (self.x + 1)]) #move top right
        self.moves.append([(self.y + 1), (self.x + 1)]) #move bottom right
        self.moves.append([(self.y + 1), (self.x - 1)]) #move bottom left

        self.remove_invalid(board, white_moves, black_moves, pieces)


        if self.color == "b": #black king

            for move in self.moves:
                if move in white_moves:
                    self.moves.remove(move) 
                try:
                    bottom_right = board[(move[0] + 1), (move[1] + 1)]
                    bottom_left = board[(move[0] + 1), (move[1] - 1)]
                    if "wp" in bottom_right or "wp" in bottom_left: #if there is a pawn ready to attack from the bottom right or bottom left
                        self.moves.remove(move)
                except:
                    pass
            self.add_moves(black_moves, white_moves)
            if black_moves == [] and self.moves == []: #if no moves available, aka checkmate
                print("Checkmate! White wins.")

        else: #white king
            
            for move in self.moves:
                if move in black_moves:
                    self.moves.remove(move)
                try:
                    top_right = board[(move[0] - 1), (move[1] + 1)]
                    top_left = board[(move[0] - 1), (move[1] - 1)]
                    if "bp" in top_right or "bp" in top_left: #if there is a pawn ready to attack from the top right or top left
                        self.moves.remove(move)
                except:
                    pass
            self.add_moves(black_moves, white_moves)
            if white_moves == [] and self.moves == []:
                print("Checkmate! Black wins.")

            
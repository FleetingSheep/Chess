import numpy
from Piece import Piece, get_selected

class King(Piece): #inherits the piece class
    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = []
        
        if self.has_moved == False: #castling

            if pieces[f"{self.color}r1"].has_moved == False: #castling to the left
                if board[self.y, (self.x - 1)] == '' and board[self.y, (self.x - 2)] == '' and board[self.y, (self.x - 3) == '']: #if space uninterrupted

                    if self.color == "b":
                        if board[self.y, (self.x - 1)] not in white_moves and board[self.y, (self.x - 2)] not in white_moves and board[self.y, (self.x - 3)] not in white_moves: #if not moving through check
                           self.moves.append([self.y, (self.x - 3)])
                           #print("left black castle")
                    else:
                        if board[self.y, (self.x - 1)] not in black_moves and board[self.y, (self.x - 2)] not in black_moves and board[self.y, (self.x - 3)] not in black_moves: #if not moving through check
                            self.moves.append([self.y, (self.x - 3)])
                            #print("left white castle")

            if pieces[f"{self.color}r2"].has_moved == False: #castling to the right
                if board[self.y, (self.x + 1)] == '' and board[self.y, (self.x + 2)] == '': #if space uninterrupted

                    if self.color == "b":
                        if board[self.y, (self.x + 1)] not in white_moves and board[self.y, (self.x + 2)] not in white_moves: #if not moving through check
                           self.moves.append([self.y, (self.x + 2)])
                           #print("right black castle")
                    else:
                        if board[self.y, (self.x - 1)] not in black_moves and board[self.y, (self.x + 2)] not in black_moves: #if not moving through check
                            self.moves.append([self.y, (self.x + 2)])
                            #print("right white castle")
        
        
        self.moves.append([self.id, (self.y + 1), (self.x)]) #move down
        self.moves.append([self.id, (self.y - 1), (self.x)]) #move up
        self.moves.append([self.id, (self.y), (self.x - 1)]) #move left
        self.moves.append([self.id, (self.y), (self.x + 1)]) #move right
        self.moves.append([self.id, (self.y - 1), (self.x - 1)]) #move top left
        self.moves.append([self.id, (self.y - 1), (self.x + 1)]) #move top right
        self.moves.append([self.id, (self.y + 1), (self.x + 1)]) #move bottom right
        self.moves.append([self.id, (self.y + 1), (self.x - 1)]) #move bottom left

        self.remove_invalid(board)

        if self.color == "b": #black king
            for move in self.moves:
                if move in white_moves:
                    self.moves.remove(move)
                else:
                    black_moves.append(move)
    
            if black_moves == [] and self.moves == []: #if no moves available, aka checkmate
                pass #end game

        else: #white king
            self.add_moves(black_moves, white_moves)
            if white_moves == [] and self.moves == []:
                pass #end game
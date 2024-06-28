from Queen import Queen
from Piece import Piece
import numpy
class Pawn(Piece):
    
    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = []
        if self.has_moved == False: #can jump two spaces?
            if self.color == "b":
                self.moves.append([(self.y + 2), (self.x)]) #move down, for black pawns

            else:
                self.moves.append([(self.y - 2), (self.x)]) #white pawns
        


        if self.color == "b":
            if board[self.y + 1, self.x] == '0':
                self.moves.append([(self.y + 1), (self.x)]) #black pawns

            try:
                target = board[(self.y + 1), (self.x - 1)]
                if target != '0' : #if capturable piece in bottom LEFT
                    if target[0] != self.color: #if the piece is not your own, it can be captured
                        self.moves.append([(self.y + 1), (self.x - 1)])
                    
            except:
                pass

            try:
                target = board[(self.y + 1), (self.x + 1)] #if capturable piece in bottom RIGHT
                if target != '0' : #if capturable piece in bottom left
                    if target[0] != self.color: #if the piece is not your own, it can be captured
                        self.moves.append([(self.y + 1), (self.x + 1)])
                    
            except:
                pass

            
        else: #WHITE PIECES
            if board[self.y - 1, self.x] == '0':
                self.moves.append([(self.y - 1), (self.x)]) #white pawns

            try:
                target = board[(self.y - 1), (self.x - 1)]
                if target != '0' : #if capturable piece in top LEFT
                    if target[0] != self.color: #if the piece is not your own, it can be captured
                        self.moves.append([(self.y - 1), (self.x - 1)])
                    
            except:
                pass

            try:
                target = board[(self.y - 1), (self.x + 1)] #if capturable piece in bottom RIGHT
                if target != '0' : #if capturable piece in top right
                    if target[0] != self.color: #if the piece is not your own, it can be captured
                        self.moves.append([(self.y - 1), (self.x + 1)])
                    
            except:
                pass

    
        
        try:#EN PASSANT FUNCTIONALITY
            to_left = board[self.y, (self.x - 1)]
        except:
            pass
        try:
            to_right = board[self.y, (self.x + 1)]
        except:
            pass

        #EN PASSANT FUNCTIONALITY
        try:
            if to_left[1] == "p":
                if pieces[to_left].en_passant == True:
                    if self.color == "b": #black pawn
                        self.moves.append([(self.y + 1), (self.x - 1)])
                    else:
                        self.moves.append([[self.id], (self.y - 1), (self.x - 1)])
        except:
            pass

        try:
            if to_right[1] == "p":
                if pieces[to_right].en_passant == True:
                    if self.color == "b": #black pawn
                        self.moves.append([(self.y + 1), (self.x + 1)])
                    else:
                        self.moves.append([(self.y - 1), (self.x + 1)])
        except:
            pass
        
        self.remove_invalid(board, white_moves, black_moves, pieces)
        self.add_moves(black_moves, white_moves)


    def promote(self):
        '''
        if self.color == "black":
            black_queens += 1
            Queen(f"{self.color}q{black_queens}") 
        else:
            white_queens += 1
            Queen(f"{self.color}q{white_queens}")
        '''

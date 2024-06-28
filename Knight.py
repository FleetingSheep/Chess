from Piece import Piece
import numpy
class Knight(Piece):

    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = [] #theres no easy way to go about this, one axis goes back or forward 2, and the other 1
        self.moves.append([self.id, (self.y + 2), (self.x - 1)])

        self.moves.append([self.id, (self.y + 2), (self.x + 1)])

        self.moves.append([self.id, (self.y - 2), (self.x - 1)])

        self.moves.append([self.id, (self.y - 2), (self.x + 1)])

        self.moves.append([self.id, (self.y + 1), (self.x + 2)])

        self.moves.append([self.id, (self.y + 1), (self.x - 2)])

        self.moves.append([self.id, (self.y - 1), (self.x - 2)])

        self.moves.append([self.id, (self.y - 1), (self.x + 2)])

        self.remove_invalid(board)
        self.add_moves(black_moves, white_moves)
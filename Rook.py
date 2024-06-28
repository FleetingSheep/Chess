from Piece import Piece
import numpy
class Rook(Piece):

    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = []

        self.check_horizontal(board)
        self.remove_invalid(board)
        self.add_moves(black_moves, white_moves)

from Piece import Piece
import numpy
class Queen(Piece):

    def get_moves(self, board, white_moves, black_moves, pieces):
        self.moves = []

        self.check_horizontal(board)
        self.check_diagonal(board)
        self.remove_invalid(board, white_moves, black_moves, pieces)
        self.add_moves(black_moves, white_moves)
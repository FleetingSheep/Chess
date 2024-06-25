from Piece import Piece
import numpy
class Bishop(Piece):

    def get_moves(self, board, white_moves, black_moves):
        self.moves = []

        self.check_diagonal(board)
        self.remove_invalid(board)
        self.add_moves(black_moves, white_moves)
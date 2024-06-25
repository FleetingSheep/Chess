import numpy


board = numpy.full((8, 8), "hi", dtype="<U6")

print(board)

move = ["id", 0, 1]
print(board[move[1], move[2]])

import pygame
import numpy
from Board import draw_board
from Piece import Piece
from Pawn import Pawn
from Rook import Rook
from Queen import Queen
from Knight import Knight
from Bishop import Bishop
from King import King

#naming: black pawn is bp, white pawn is wp, and so on...

pieces = {}
board = None

black_queens = 1 #number of queens, so that promoted pawns have unique IDs
white_queens = 1

most_recent = None #for checking validity of en passant

pygame.init()
window_height, window_width = 1280, 1280
screen = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()            

white_moves = [] #to check valid king moves and determine if there is checkmate
black_moves = []
        

def setup_board(board_size): #place pieces
    global board
    board = numpy.full((board_size, board_size), 0, dtype="<U6") #create empty 8x8 board
    #rooks
    board[0, 0] = "br1"
    board[0, 7] = "br2"

    board[7, 0] = "wr1"
    board[7, 7] = "wr2"

    #knights
    board[0, 1] = "bn1"
    board[0, 6] = "bn2"

    board[7, 1] = "wn1"
    board[7, 6] = "wn2"

    #bishops
    board[0, 2] = "bb1"
    board[0, 5] = "bb2"

    board[7, 2] = "wb1"
    board[7, 5] = "wb2"

    #queens
    board[0, 3] = "bq"
    board[7, 3] = "wq"

    #kings
    board[0, 4] = "bk"
    board[7, 4] = "wk"

    for space, i in enumerate(board[6]): #create white pawns
        board[6, space] = f"wp{space + 1}"
    for space, i in enumerate(board[1]): #create black pawns
        board[1, space] = f"bp{space + 1}"
    
    for column, row in enumerate(board): #initialize sprites for pieces
        for space, i in enumerate(row):
            if i != '0':

                type = i[1]

                match type:

                    case "r": #rook
                        x = Rook(i, [column, space], "rook")
                    case "n": #knight
                        x = Knight(i, [column, space], "knight")
                    case "b": #bishop
                        x = Bishop(i, [column, space], "bishop")
                    case "k": #king
                        x = King(i, [column, space], "king")
                    case "q":  #queen
                        x = Queen(i, [column, space], "queen")
                    case "p": #pawn
                        x = Pawn(i, [column, space], "pawn")
                x.move_to_start()
                pieces[x.id] = x

    print(board)

screen.fill("white")
setup_board(8)
draw_board(window_height, window_width, 8, screen)

piece_group = pygame.sprite.Group()

counter = 1 #REMOVE

pending_move = True #waiting for move, don't recalculate moves unless one has actually been made!
turn = "w"
while True:
    if pending_move == True:
        white_moves = [] #to check valid king moves and determine if there is checkmate
        black_moves = []

        for item in pieces.values():
            if item.id[1] != "k": #ignore king moves at first so we can check theirs later (so they dont move into check)
                item.get_moves(board, white_moves, black_moves)
            pygame.sprite.Group.add(piece_group, item)

        for item in pieces.values():
            if item.id[1] == "k":
                item.get_moves(board, white_moves, black_moves)
    '''
    if counter == 1:
        print(f"white moves: {white_moves}")
        print(f"black moves: {black_moves}")
        counter += 1
    '''

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    piece_group.update(events) #to check for clicks...
    piece_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)


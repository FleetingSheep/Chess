
import pygame
import numpy
from Board import draw_board
from Piece import Piece, get_selected, turn_false
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

red = pygame.Color(255, 0, 0)       

class Highlighter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = f"highlight.png"
        self.image = pygame.image.load(f"{self.image}")
        self.image = pygame.transform.scale(self.image, (160, 160))
        self.rect = self.image.get_rect()
    

    def move(self, id):
        piece = pieces[id]
        self.rect.x = piece.get_x()
        self.rect.y = piece.get_y()

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

piece_group = pygame.sprite.Group()

pending_move = True #waiting for move, don't recalculate moves unless one has actually been made!
turn = "w"

highlighter = Highlighter()
highlight_group = pygame.sprite.Group()
pygame.sprite.Group.add(highlight_group, highlighter)

piece_selected = True
setup_board(8)
for item in pieces.values():
            pygame.sprite.Group.add(piece_group, item)

if_piece_selected = False
while True:
    if pending_move == True:
        white_moves = [] #to check valid king moves and determine if there is checkmate
        black_moves = []

        for item in pieces.values():
            if item.id[1] != "k": #ignore king moves at first so we can check theirs later (so they dont move into check)
                item.get_moves(board, white_moves, black_moves, pieces)
            if item.id[1] == "k":
                item.get_moves(board, white_moves, black_moves, pieces)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(if_piece_selected)
            if if_piece_selected == True:

                piece = pieces[piece_selected[1]] #grab class object for piece
                x = int(event.pos[0] / 160)
                y = int(event.pos[1] / 160)
                
                for move in piece.moves:

                    if move[0] == y and move[1] == x: #if the cursor clicks on the correct tile for a move

                        if board[y, x] != '0': # capture a piece?

                            captured_piece = pieces[board[y, x]]
                            pieces.pop(captured_piece.id)
                            pygame.sprite.Group.remove(piece_group, captured_piece)

                        if piece.id[1] == "p": #if pawn
                            if board[y, x] == '0': #if space empty
                                if abs(piece.x - x) == 1 and abs(piece.y - y) == 1: #if the pawn moved diagonally one space, but did not take anything!

                                    if piece.color == "b":
                                        captured_piece = pieces[board[(y - 1), x]]
                                    else:
                                        captured_piece = pieces[board[(y + 1), x]]
                                    pieces.pop(captured_piece.id)
                                    pygame.sprite.Group.remove(piece_group, captured_piece)

                        board[piece.y, piece.x] = '0' #make sure the piece leaves behind an empty space
                        board[y, x] = piece.id

                        if piece.id[1] == "k": #check if the move is a castle and move the rook accordingly!
                            if abs(piece.x - x) > 1: #if the move had the king go more than one space (a castle)
                                
                                if x > 4: #right side of the board, so move the right rook
                                    chosen_rook = pieces[f"{piece.color}r2"]
                                    board[chosen_rook.y, chosen_rook.x] = '0'
                                    chosen_rook.x -= 2
       
                                else: #left side of the board, so move the left rook
                                    chosen_rook = pieces[f"{piece.color}r1"]
                                    board[chosen_rook.y, chosen_rook.x] = '0'
                                    chosen_rook.x += 3
                                    
                                board[chosen_rook.y, chosen_rook.x] = chosen_rook.id
                                rook_x = chosen_rook.get_x()
                                rook_y = chosen_rook.get_y()
                                chosen_rook.rect.x = rook_x
                                chosen_rook.rect.y = rook_y

                        piece.x = x
                        piece.y = y

                        

                        x = piece.get_x()
                        y = piece.get_y()

                        piece.rect.x = x
                        piece.rect.y = y

                        if_piece_selected = False
                        if turn == "w":
                            turn = "b"
                        else:
                            turn = "w"
                        turn_false()
                        print(board)
                        piece.has_moved = True

                        for chosen_piece in pieces.values(): #after a move has passed, make sure en passant doesnt trigger, unless the most recent move was a double jump by that pawn
                            chosen_piece.en_passant = False

                        if piece.id[1] == "p":
                            if abs(piece.y - y) > 1: #if the move was a double jump from the pawn, enable en passant
                                piece.en_passant = True
                            else:
                                pass

    screen.fill(red)
    draw_board(window_height, window_width, 8, screen)

    piece_group.update(events, turn, highlighter) #to check for clicks...
    piece_group.draw(screen)
    piece_selected = get_selected()
    if_piece_selected = piece_selected[0]
    if if_piece_selected == True:
        highlight_group.update(events, turn, highlighter)
        highlight_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)


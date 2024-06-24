
import pygame
import numpy
import itertools
from Board import draw_board
from Piece import Piece

#naming: black pawn is bp, white pawn is wp, and so on...

pieces = {}
board = numpy.full((8, 8), "", dtype="<U6")

black_queens = 1 #number of queens, so that promoted pawns have unique IDs
white_queens = 1

pygame.init()
window_height, window_width = 1280, 1280
screen = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)              

white_moves = [] #to check valid king moves and determine if there is checkmate
black_moves = []

class King(Piece): #inherits the piece class
    def get_moves(self):
        self.moves = []
        if self.has_moved == False: #castling

            if pieces[f"{self.color}r1"].has_moved == False: #castling to the left
                if board[self.y, (self.x - 1)] == '' and board[self.y, (self.x - 2)] == '' and board[self.y, (self.x - 3) == '']: #if space uninterrupted

                    if self.color == "b":
                        if board[self.y, (self.x - 1)] not in white_moves and board[self.y, (self.x - 2)] not in white_moves and board[self.y, (self.x - 3)] not in white_moves: #if not moving through check
                           self.moves.append([self.y, (self.x - 3)]) 
                    else:
                        if board[self.y, (self.x - 1)] not in black_moves and board[self.y, (self.x - 2)] not in black_moves and board[self.y, (self.x - 3)] not in black_moves: #if not moving through check
                            self.moves.append([self.y, (self.x - 3)])

            if pieces[f"{self.color}r2"].has_moved == False: #castling to the right
                if board[self.y, (self.x + 1)] == '' and board[self.y, (self.x + 2)] == '': #if space uninterrupted

                    if self.color == "b":
                        if board[self.y, (self.x + 1)] not in white_moves and board[self.y, (self.x + 2)] not in white_moves: #if not moving through check
                           self.moves.append([self.y, (self.x + 2)]) 
                    else:
                        if board[self.y, (self.x - 1)] not in black_moves and board[self.y, (self.x + 2)] not in black_moves: #if not moving through check
                            self.moves.append([self.y, (self.x + 2)])
        
        self.moves.append([(self.y + 1), (self.x)]) #move up
        self.moves.append([(self.y - 1), (self.x)]) #move down
        self.moves.append([(self.y), (self.x - 1)]) #move left
        self.moves.append([(self.y), (self.x + 1)]) #move right
        self.moves.append([(self.y - 1), (self.x - 1)]) #move bottom left
        self.moves.append([(self.y - 1), (self.x + 1)]) #move bottom right
        self.moves.append([(self.y + 1), (self.x + 1)]) #move top right
        self.moves.append([(self.y + 1), (self.x - 1)]) #move top left

        self.remove_invalid()

        if self.color == "b":
            for move in self.moves:
                if move in white_moves:
                    self.moves.remove(move)
            if black_moves == [] and self.moves == []: #if no moves available, aka checkmate
                pass #end game
        else: #white
            for move in self.moves:
                if move in black_moves:
                    self.moves.remove(move)
            if white_moves == [] and self.moves == []:
                pass #end game

class Queen(Piece):
    def get_moves(self):
        self.moves = []

class Rook(Piece):
    def get_moves(self):
        self.moves = []

class Knight(Piece):
    def get_moves(self):
        self.moves = []

class Bishop(Piece):
    def get_moves(self):
        self.moves = []

class Pawn(Piece):
    def get_moves(self):
        self.moves = []
        if self.has_moved == False:
            pass



    def promote(self):
        global black_queens, white_queens

        if self.color == "black":
            black_queens += 1
            Queen(f"{self.color}q{black_queens}") 
        else:
            white_queens += 1
            Queen(f"{self.color}q{white_queens}")




def setup_board(board_size): #place pieces

    board = numpy.full((board_size, board_size), "", dtype="<U6") #create empty 8x8 board
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
            if i != '':

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


screen.fill("white")
setup_board(8)
draw_board(window_height, window_width, 8, screen)

piece_group = pygame.sprite.Group()


while True:

    white_moves = [] #to check valid king moves and determine if there is checkmate
    black_moves = []

    for item in pieces.values():
        if item.id[1] != "k": #ignore king moves at first so we can check theirs later
            item.get_moves()
        pygame.sprite.Group.add(piece_group, item)

    for item in pieces.values():
        if item.id[1] == "k":
            item.get_moves()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    piece_group.update(events) #to check for clicks...
    piece_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)
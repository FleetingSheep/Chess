
import pygame
import numpy
import itertools

#naming: black pawn is bp, white pawn is wp, and so on...

pieces = {}

pygame.init()
window_height, window_width = 1280, 1280
screen = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
altblack = pygame.Color(202, 93, 43)
altwhite = pygame.Color(249, 214, 177)

class Piece(pygame.sprite.Sprite):

    def __init__(self, id, pos, image):

        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.pos = pos
        self.x = pos[1]
        self.y = pos[0]
        self.image = image
        self.color = self.id[0]

        if self.color == "b":
            self.color = "black"
        else:
            self.color = "white"
        self.image = f"{self.color}{self.image}.png"
        self.image = pygame.image.load(f"{self.image}")
        self.image = pygame.transform.scale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        

    def __repr__(self):
        return f"ID: {self.id}, POS: {self.pos}"
    
    def get_captured(self):
        pieces.pop(self.id)

class King(Piece):
    def get_moves(self):
        moves = []
class Queen(Piece):
    def get_moves(self):
        moves = []
class Rook(Piece):
    def get_moves(self):
        moves = []
class Knight(Piece):
    def get_moves(self):
        moves = []
class Bishop(Piece):
    def get_moves(self):
        moves = []
class Pawn(Piece):
    def get_moves(self):
        moves = []




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
    board[0, 3] = "bq1"
    board[7, 3] = "wq2"

    #kings
    board[0, 4] = "bk1"
    board[7, 4] = "wk2"

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

                pieces[x.id] = x



def draw_board(window_height, window_width, board_size):#draw bg tiles

    tile_height = window_height // board_size
    tile_width = window_width // board_size

    counter = 0 #move down one tile after filling all 8 in a horizontal row
    offset = False #create checkered pattern by starting with either black or white

    for i in range(board_size): #two nested loops, deepest loop draws horizontally while outermost loop (this one) moves down one tile

        escape_counter = 0 #escape horizontal loop

        tile_height = window_height // board_size
        tile_width = window_width // board_size


        for color_1 in itertools.cycle('AB'): #cycle between
            if color_1 == 'A':
                if offset == True:
                    color_choice = altblack
                else:
                    color_choice = altwhite
            elif color_1 == 'B':
                if offset == True:
                    color_choice = altwhite
                else:
                    color_choice = altblack

            tile = pygame.Rect(tile_width * (escape_counter), tile_height * counter, tile_height, tile_width)
            pygame.Surface.fill(screen, color_choice, rect=tile)
            escape_counter += 1
            if escape_counter >= 9:
                break
        

        counter += 1
        if offset == False:
            offset = True
        else:
            offset = False

screen.fill("white")
setup_board(8)
draw_board(window_height, window_width, 8)

piece_group = pygame.sprite.Group()
for item in pieces.values():
        pygame.sprite.Group.add(piece_group, item)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    piece_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)
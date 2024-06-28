import pygame
is_piece_selected = False
chosen_piece = None
class Piece(pygame.sprite.Sprite):

    def __init__(self, id, pos, image):

        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.pos = pos
        self.x = pos[1]
        self.y = pos[0]
        self.image = image
        self.color = self.id[0]
        self.has_moved = False
        self.selected = False
        self.en_passant = False

        if self.color == "b":
            self.color_str = "black"
        else:
            self.color_str = "white"

        self.image = f"{self.color_str}{self.image}.png"
        self.image = pygame.image.load(f"{self.image}")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

    def remove_invalid(self, board, white_moves, black_moves, pieces):
        targeted_removal = []
        for move in range(len(self.moves)):
            move = self.moves[move - 1]
            try:
                if move[0] > 7 or move[1] > 7 or move[0] < 0 or move[1] < 0: #if outside of the board

                    targeted_removal.append(move)

                else:
                    tempy = move[0]
                    tempx = move[1]

                    if board[tempy, tempx] != '0': #if space is not empty, consider making it invalid
                        temp = board[tempy, tempx]
                        #print(temp[0])
                        if temp[0] == self.color: #if space contains a piece of the same color, remove!
                            targeted_removal.append(move)
            except:
                targeted_removal.append(move)
        
        for move in targeted_removal:
            self.moves.remove(move)


    '''
        targeted_removal = []
        for move in range(len(self.moves)):

            future = board #simulate the move the player is making, and ensure it does not put the king in check
            future[self.y, self.x] = '0' #make sure the piece leaves behind an empty space

            move = self.moves[move - 1]

            future[move[1], move[2]] = self.id

            for item in pieces.values():
                if item.id[1] != "k": #ignore king moves at first so we can check theirs later (so they dont move into check)
                    item.get_moves(future, white_moves, black_moves, pieces)
                if item.id[1] == "k":
                    item.get_moves(future, white_moves, black_moves, pieces)


            if self.color== "b": #if black's turn, make sure whatever they did didn't reveal the king
                king = pieces["wk"]
                if [king.y, king.x] in white_moves:
                    targeted_removal.append(move)
            else:
                king = pieces["bk"]
                if [king.y, king.x] in black_moves:
                    targeted_removal.append(move)

        for move in targeted_removal:
            self.moves.remove(move)
    '''

    def add_moves(self, black_moves, white_moves):
        for move in self.moves:
                if move in black_moves:
                    self.moves.remove(move)
                else:
                    if self.color == "b":
                        black_moves.append(move)
                    else:
                        white_moves.append(move)


    def check_horizontal(self, board): #check if there is nothing inbetween the piece and its destination, for rooks, queens
        cursor_x = self.x #for checking valid tiles
        cursor_y = self.y

        while cursor_x < 7: #right
            cursor_x += 1
            if board[self.y, cursor_x] == '0':
                self.moves.append([self.y, cursor_x])
            else:
                temp = board[self.y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([self.y, cursor_x])
                else:
                    break
        cursor_x = self.x

        while cursor_x > 0: #left
            cursor_x -= 1
            if board[self.y, cursor_x] == '0':
                self.moves.append([self.y, cursor_x])
            else:
                temp = board[self.y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([self.y, cursor_x])
                else:
                    break
        
        while cursor_y > 0: #up
            cursor_y -= 1
            if board[cursor_y, self.x] == '0':
                self.moves.append([cursor_y, self.x])
            else:
                temp = board[cursor_y, self.x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, self.x])
                else:
                    break

        cursor_y = self.y
        while cursor_y < 7: #down
            cursor_y += 1
            if board[cursor_y, self.x] == '0':
                self.moves.append([cursor_y, self.x])
            else:
                temp = board[cursor_y, self.x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, self.x])
                else:
                    break
    
    def check_diagonal(self, board): #for bishops and queens
        
        cursor_x = self.x
        cursor_y = self.y

        while cursor_x < 7 and cursor_y < 7: #bottom right
            cursor_x += 1
            cursor_y += 1
            if board[cursor_y, cursor_x] == '0':
                self.moves.append([cursor_y, cursor_x])
            else:
                temp = board[cursor_y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, cursor_x])
                else:
                    break

        cursor_x = self.x
        cursor_y = self.y

        while cursor_x > 0 and cursor_y < 7: #top left
            cursor_x -= 1
            cursor_y += 1
            if board[cursor_y, cursor_x] == '0':
                self.moves.append([cursor_y, cursor_x])
            else:
                temp = board[cursor_y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, cursor_x])
                else:
                    break
        cursor_x = self.x
        cursor_y = self.y

        while cursor_x > 0 and cursor_y > 0: #bottom left
            cursor_x -= 1
            cursor_y -= 1
            if board[cursor_y, cursor_x] == '0':
                self.moves.append([cursor_y, cursor_x])
            else:
                temp = board[cursor_y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, cursor_x])
                else:
                    break
        cursor_x = self.x
        cursor_y = self.y

        while cursor_x < 7 and cursor_y > 0: #bottom right
            cursor_x += 1
            cursor_y -= 1
            if board[cursor_y, cursor_x] == '0':
                self.moves.append([cursor_y, cursor_x])
            else:
                temp = board[cursor_y, cursor_x]
                if temp[0] != self.color:
                    self.moves.append([cursor_y, cursor_x])
                else:
                    break
        cursor_x = self.x
        cursor_y = self.y
            

    def __repr__(self):
        return f"ID: {self.id}, POS: {self.pos}"
        

    def get_x(self):
        return (self.x * 160) + 3
    def get_y(self):
        return (self.y * 160)
    
    def move_to_start(self):
        self.rect.x = (160 * self.x) + 3
        self.rect.y = 160 * self.y

    def get_moves(self): #decoy function so that it can be overridden by child class?
        pass
    
    def update(self, events, turn, highlighter):
        global is_piece_selected, chosen_piece
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if turn == self.color:
                        if is_piece_selected == False:
                            if self.moves != []:
                                #print(self.id)
                                chosen_piece = self.id
                                self.selected = True
                                is_piece_selected = True
                                highlighter.move(chosen_piece)
                        

                    
def get_selected():
    global is_piece_selected, chosen_piece
    piece_selected = [is_piece_selected, chosen_piece]
    return piece_selected

def turn_false():
    global is_piece_selected
    is_piece_selected = False

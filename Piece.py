import pygame

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
        self.moves = []

        if self.color == "b":
            self.color_str = "black"
        else:
            self.color_str = "white"
        self.image = f"{self.color_str}{self.image}.png"
        self.image = pygame.image.load(f"{self.image}")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

    def remove_invalid(self):
        for move in self.moves:
            if move[0] > 7 or move[1] > 7 or move[0] < 0 or move[1] < 0: #if outside of the board
                self.moves.pop(move)
    
    def check_horizontal(self, board): #check if there is nothing inbetween the piece and its destination, for rooks, queens
        cursor_x = self.x #for checking valid tiles
        cursor_y = self.y

        while cursor_x < 8: #right
            cursor_x += 1
            if board[self.y, cursor_x] == '':
                self.moves.append(board[self.y, cursor_x])
            else:
                break
        cursor_x = self.x
        while cursor_x > -1: #left
            cursor_x -= 1
            if board[self.y, cursor_x] == '':
                self.moves.append(board[self.y, cursor_x])
            else:
                break

        while cursor_y > -1: #down
            cursor_y -= 1
            if board[cursor_y, self.x] == '':
                self.moves.append(board[cursor_y, self.x])
            else:
                break
        cursor_y = self.y
        while cursor_x < 8: #up
            cursor_x += 1
            if board[cursor_y, self.x] == '':
                self.moves.append(board[cursor_y, self.x])
            else:
                break
    
    def check_diagonal(self): #for bishops and queens
        
        cursor_x = self.x
        cursor_y = self.y

        #while cursor_x < 8 and cursor_y < 8: #top right
            

    def __repr__(self):
        return f"ID: {self.id}, POS: {self.pos}"
    
    def get_captured(self):
        #pieces.pop(self.id)
        pass

    def get_x(self):
        return (self.x * 160) + 3
    def get_y(self):
        return (self.y * 160)
    def move_to_start(self):
        self.rect.x = (160 * self.x) + 3
        self.rect.y = 160 * self.y

    def get_moves(self): #decoy function so that it can be overridden by child class?
        pass
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    #moving_x = (event.pos[0])
                    #moving_y = (event.pos[1])

                    #self.rect.x = moving_x
                    #self.rect.y = moving_y
                    self.get_moves()
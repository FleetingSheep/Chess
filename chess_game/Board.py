import pygame
class Board:

    def __init__(self, tile_width, tile_height, board_size):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.board_size = board_size
        self.white = pygame.Color(255, 255, 255)
        self.black = pygame.Color(0, 0, 0)

    def handle_click(self, pos):
        pass

    def draw(self, screen):
        board = pygame.Surface(self.tile_width, self.tile_height)
        board.fill(self.white)
        for x in range(0, 8, 2):
            for y in range(0, 8, 2):
                pygame.draw.rect(board, self.black, (x*self.tile_width, y*self.tile_width, self.tile_width, self.tile_width))
            
        


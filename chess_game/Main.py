import pygame
from Board import Board
from Game import Game

pygame.init()
window_height = 1280
window_width = 1280
screen = pygame.display.set_mode((window_width, window_height))

class Chess:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.FPS = pygame.time.Clock()
        pygame.display.set_caption("Mark's Chess")


    def _draw(self, board):
        board.draw(self.screen)
        pygame.display.update()


    def main(self, window_width, window_height):
        board_size = 8 #8 width 8 height
        tile_width, tile_height = window_width // board_size, window_height // board_size #adjust board dimensions according to window size
        board = Board(tile_width, tile_height, board_size) #board setup
        game = Game() #runtime

        while self.running:
            game.check_jump(board)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
                if not game.is_game_over(board):
                    if self.event.type == pygame.MOUSEBUTTONDOWN:
                        board.handle_click(self.event.pos)
                else:
                    game.message()
                    self.running = False

            self._draw(screen) #screen doesnt automatically maintain itself, it has to be FORCED to refresh the screen by drawing it, creating the impression of continuity
            self.FPS.tick(60) #wait until next frame at 60fps



mygame = Chess(screen)

mygame.main(window_width, window_height)


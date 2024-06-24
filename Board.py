import itertools
import pygame
def draw_board(window_height, window_width, board_size, screen):#draw bg tiles
    altblack = pygame.Color(202, 93, 43)
    altwhite = pygame.Color(249, 214, 177)
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


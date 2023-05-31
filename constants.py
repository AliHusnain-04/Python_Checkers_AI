import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
PURPLE = (128,0,128)
INDIGO = (75,0,130)
MIDNIGHTBLUE = (25,25,112)
NAVY = (0,0,128)
ORANGE = (255,69,0)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

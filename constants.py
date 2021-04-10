import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
ROWS, COLS = 6, 7

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "icon.png")))

SIDE_SPACE = WIDTH / 8
TOP_SPACE = HEIGHT / 6
STAND_HEIGHT = HEIGHT - TOP_SPACE
STAND_WIDTH = WIDTH - SIDE_SPACE * 2

SECTION_HEIGHT = STAND_HEIGHT / 6
SECTION_WIDTH = STAND_WIDTH / 7

CHECKER_RADIUS = SECTION_HEIGHT/2-10

FPS = 60
WHITE = (255, 255, 255)
BLUE = (38, 134, 212)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (153, 159, 163)

RESET = pygame.font.SysFont('arial', 25).render("RESET", True, BLACK)
VICTORY = pygame.font.SysFont('comicsans', 100)

DROP = pygame.mixer.Sound(os.path.join("assets", "drop.mp3"))

BOARD = pygame.image.load(os.path.join("assets", "board.png"))

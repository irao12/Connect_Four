from constants import *
from game import Game
import sys

pygame.font.init()


def draw_circle(row, col, color):
    pygame.draw.circle(WIN, color,
                       (SIDE_SPACE + col * SECTION_WIDTH + SECTION_WIDTH / 2,
                        TOP_SPACE + row * SECTION_HEIGHT + SECTION_HEIGHT / 2),
                       CHECKER_RADIUS)


def draw_cursor(pos, checker_color):
    x, y = pos
    if x <= SIDE_SPACE:
        x = SIDE_SPACE
    if x >= WIDTH - SIDE_SPACE:
        x = WIDTH - SIDE_SPACE - SECTION_WIDTH
    x_value = ((x - SIDE_SPACE) // SECTION_WIDTH) * SECTION_WIDTH + SIDE_SPACE + SECTION_WIDTH / 2
    if checker_color == 1:
        color = BLACK
    else:
        color = RED
    pygame.draw.circle(WIN, color, (x_value, SECTION_WIDTH / 2), CHECKER_RADIUS)


def draw_victory(turn_col):
    if turn_col == 1:
        victor = "BLACK"
    else:
        victor = "RED"
    message = victor + " WON!"
    message_font = VICTORY.render(message, 1, BLACK)
    message_border = pygame.Rect(WIDTH/2 - message_font.get_width()/2, HEIGHT/2 - message_font.get_height()/2,
                                 message_font.get_width(), message_font.get_height())
    pygame.draw.rect(WIN, GRAY, message_border)
    WIN.blit(message_font, (WIDTH/2 - message_font.get_width()/2, HEIGHT/2 - message_font.get_height()/2))


def draw_tie():
    message_font = VICTORY.render("DRAW", 1, BLACK)
    message_border = pygame.Rect(WIDTH / 2 - message_font.get_width() / 2, HEIGHT / 2 - message_font.get_height() / 2,
                                 message_font.get_width(), message_font.get_height())
    pygame.draw.rect(WIN, GRAY, message_border)
    WIN.blit(message_font, (WIDTH / 2 - message_font.get_width() / 2, HEIGHT / 2 - message_font.get_height() / 2))


def draw_window(stand, pos, checker_color, game):
    WIN.fill((255, 255, 255))

    for row in range(ROWS):
        for col in range(COLS):
            if stand.checkers[row][col] == 1:
                draw_circle(row, col, BLACK)
            elif stand.checkers[row][col] == 2:
                draw_circle(row, col, RED)

    WIN.blit(BOARD, (SIDE_SPACE, TOP_SPACE))

    if not game.finished:
        draw_cursor(pos, checker_color)
    reset_border = pygame.Rect(0+5, 0+5, RESET.get_width(), RESET.get_height())
    pygame.draw.rect(WIN, GRAY, reset_border)
    WIN.blit(RESET, (0+5, 0+5))

    if game.finished:
        if game.turn_num < 43:
            draw_victory(game.turn_col)
        else:
            draw_tie()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    game = Game()

    while run:
        clock.tick(FPS)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                reset_border = pygame.Rect(0 + 5, 0 + 5, RESET.get_width(), RESET.get_height())
                if reset_border.collidepoint(pos):
                    game.reset()
                if not game.finished:
                    game.finished = game.drop_checkers(pos)
        draw_window(game.stand, pos, game.turn_col, game)


main()

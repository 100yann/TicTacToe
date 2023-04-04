import sys
import pygame
from engine import TicTacToe

# Initialize Pygame screen
pygame.init()


font1 = pygame.font.SysFont('arialblack', 40)
font2 = pygame.font.SysFont('arialblack', 25)

TEXT_COL = (250, 250, 250)


game_on = True
while True:
    start_game = TicTacToe()
    if start_game.check_win():
        game_on = False
        player = start_game.check_win()[1]
        start_game.endgame_screen(f'Game over! {player} wins.', font1, TEXT_COL, 250, 875)
        start_game.endgame_screen('Press "R" to retry or "Q" to quit', font2, TEXT_COL, 237, 925)
        if start_game.replay():
            game_on = True
    elif start_game.check_win() == 0:
        game_on = False
        start_game.endgame_screen("It's a draw.", font1, TEXT_COL, 320, 875)
        start_game.endgame_screen('Press "R" to retry or "Q" to quit', font2, TEXT_COL, 237, 925)
        if start_game.replay():
            game_on = True
    start_game.check_events(game_on)
    pygame.display.update()

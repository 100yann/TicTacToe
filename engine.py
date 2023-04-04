import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 1000))

BACKGROUND = pygame.image.load('background.png')
pygame.display.set_caption('Tic Tac Toe')
IMG_X = pygame.image.load('x.png')
IMG_O = pygame.image.load('o.png')

array = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

coordinates = [(20, 20), (320, 20), (620, 20),
               (20, 320), (320, 320), (620, 320),
               (20, 620), (320, 620), (620, 620)]

font1 = pygame.font.SysFont('arialblack', 40)
font2 = pygame.font.SysFont('arialblack', 25)

TEXT_COL = (250, 250, 250)
player = "X"


class TicTacToe:
    def __init__(self):
        screen.blit(BACKGROUND, (0, 0))

    def draw_elements(self):
        for i, x in enumerate(array):
            if array[i] == 'X':
                screen.blit(IMG_X, (coordinates[i][0], coordinates[i][1]))
            elif array[i] == "O":
                screen.blit(IMG_O, (coordinates[i][0], coordinates[i][1]))

    def check_events(self, game_on):
        turn = font2.render(f"It's {player}'s turn.", font2, TEXT_COL)
        screen.blit(turn, (20, 920))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_on:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    self.check_click(x, y)
        self.draw_elements()


    def change_player(self):
        global player
        if player == "X":
            player = "O"
        else:
            player = "X"

    def check_click(self, x, y):
        print(x,y)
        for index, tuple in enumerate(coordinates):
            if x <= tuple[0] + 280 and y <= tuple[1] + 280:
                    if array[index] == "-":
                        array[index] = player
                        if "-" not in array:
                            pass
                        elif self.check_win():
                            break
                        else:
                            self.change_player()
                    break

    def check_win(self):
        # checking rows
        for int in range(0, 9, 3):
            if array[int] != '-' and array[int] == array[int + 1] and array[int + 1] == array[int + 2]:
                line_x_start = coordinates[int][0]
                line_x_end = coordinates[int][0] + 800
                line_y = coordinates[int][1] + 130
                pygame.draw.line(screen,
                                 color=(255, 255, 255),
                                 start_pos=[line_x_start, line_y],
                                 end_pos=[line_x_end, line_y],
                                 width=20)
                return True, player
        # checking columns
        for int in range(0, 3):
            if array[int] != '-' and array[int] == array[int + 3] and array[int + 3] == array[int + 6]:
                line_x = coordinates[int][0] + 130
                line_y_start = coordinates[int][1]
                line_y_end = coordinates[int][1] + 800
                pygame.draw.line(screen,
                                 color=(255, 255, 255),
                                 start_pos=[line_x, line_y_start],
                                 end_pos=[line_x, line_y_end],
                                 width=20)
                return True, player

        # checking diagonals
        if array[0] != '-' and array[0] == array[4] and array[4] == array[8]:
            pygame.draw.line(screen,
                             color=(255, 255, 255),
                             start_pos=[20, 20],
                             end_pos=[820, 820],
                             width=20)
            return True, player

        elif array[2] != '-' and array[2] == array[4] and array[4] == array[6]:
            pygame.draw.line(screen,
                             color=(255, 255, 255),
                             start_pos=[880, 20],
                             end_pos=[25, 880],
                             width=40)
            return True, player

        # Draw
        remaining_moves = 9
        for i, x in enumerate(array):
            if array[i] != '-':
                remaining_moves -= 1
                if remaining_moves == 0:
                    return remaining_moves

    def endgame_screen(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def replay(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    global array
                    array = ['-', '-', '-',
                             '-', '-', '-',
                             '-', '-', '-']
                    screen.blit(BACKGROUND, (0, 0))
                    self.change_player()
                    return True
                elif event.key == pygame.K_q:
                    sys.exit()
        else:
            return False

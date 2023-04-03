import sys
import pygame

# Initialize Pygame screen
pygame.init()

# Create screen
screen = pygame.display.set_mode((900, 1000))

bg = pygame.image.load('background.png')
pygame.display.set_caption('Tic Tac Toe')
img_x = pygame.image.load('x.png')
img_o = pygame.image.load('o.png')

array = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

coordinates = [(20, 20), (320, 20), (620, 20),
               (20, 320), (320, 320), (620, 320),
               (20, 620), (320, 620), (620, 620)]


def check_click(x, y, player):
    if x < 280:
        if y < 280:
            if array[0] == "-":
                array[0] = player
        elif y < 580:
            if array[3] == "-":
                array[3] = player
        else:
            if array[6] == "-":
                array[6] = player
    elif x < 580:
        if y < 280:
            if array[1] == "-":
                array[1] = player
        elif y < 580:
            if array[4] == "-":
                array[4] = player
        else:
            if array[7] == "-":
                array[7] = player
    elif x < 880:
        if y < 280:
            if array[2] == "-":
                array[2] = player
        elif y < 580:
            if array[5] == "-":
                array[5] = player
        else:
            if array[8] == "-":
                array[8] = player


def check_win(player):
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
            return True

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
            return True

    # checking diagonals
    if array[0] != '-' and array[0] == array[4] and array[4] == array[8]:
        pygame.draw.line(screen,
                         color=(255, 255, 255),
                         start_pos=[20, 20],
                         end_pos=[820, 820],
                         width=20)
        return True

    elif array[2] != '-' and array[2] == array[4] and array[4] == array[6]:
        print(f'{player} wins')
        pygame.draw.line(screen,
                         color=(255, 255, 255),
                         start_pos=[880, 20],
                         end_pos=[25, 880],
                         width=40)
        return True

    # Draw
    remaining_moves = 9
    for i, x in enumerate(array):
        if array[i] != '-':
            remaining_moves -= 1
            if remaining_moves == 0:
                return remaining_moves


def draw_shapes():
    for i, x in enumerate(array):
        if array[i] == 'X':
            screen.blit(img_x, (coordinates[i][0], coordinates[i][1]))
        elif array[i] == "O":
            screen.blit(img_o, (coordinates[i][0], coordinates[i][1]))


font1 = pygame.font.SysFont('arialblack', 40)
font2 = pygame.font.SysFont('arialblack', 25)

TEXT_COL = (250, 250, 250)


def reset_game(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


player = "X"
game_on = True

screen.blit(bg, (0, 0))

while True:
    draw_shapes()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_on:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                check_click(x, y, player)

                if check_win(player):
                    game_on = False
                    reset_game(f'Game over, {player} won!', font1, TEXT_COL, 250, 875)
                    reset_game('Press "R" to retry or "Q" to quit', font2, TEXT_COL, 237, 925)
                elif check_win(player) == 0:
                    reset_game("It's a draw.", font1, TEXT_COL, 325, 875)
                if player == "X":
                    player = "O"
                else:
                    player = "X"
        elif event.type == pygame.KEYDOWN and not game_on:
            if event.key == pygame.K_r:
                array = ['-', '-', '-',
                         '-', '-', '-',
                         '-', '-', '-']
                game_on = True
                screen.blit(bg, (0, 0))
                print(array)

    pygame.display.update()

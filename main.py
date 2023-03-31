import sys

import pygame

# Initialize Pygame screen
pygame.init()

# Create screen
screen = pygame.display.set_mode((900, 900))

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

def draw_win_line():
    line_x_start


def check_win(player):
    # checking rows
    for int in range(0, 9, 3):
        if array[int] != '-' and array[int] == array[int + 1] and array[int + 1] == array[int + 2]:
            line_x_start = coordinates[int][0]
            line_x_end = coordinates[int][0] + 800
            line_y = coordinates[int][1] + 130
            pygame.draw.line(screen,
                             color=(150, 179, 113),
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
                             color=(150, 179, 113),
                             start_pos=[line_x, line_y_start],
                             end_pos=[line_x, line_y_end],
                             width=20)
            return True


    # checking diagonals
    if array[0] != '-' and array[0] == array[4] and array[4] == array[8]:
        line_x = coordinates[int][0] + 130
        line_y_start = coordinates[int][1]
        line_y_end = coordinates[int][1] + 800
        pygame.draw.line(screen,
                         color=(150, 179, 113),
                         start_pos=[line_x, line_y_start],
                         end_pos=[line_x, line_y_end],
                         width=20)
        return True, int
    elif array[2] != '-' and array[2] == array[4] and array[4] == array[6]:
        print(f'{player} wins')
        return True,

    # Draw
    remaining_moves = 9
    for i, x in enumerate(array):
        if array[i] != '-':
            remaining_moves -= 1
            if remaining_moves == 0:
                print("It's a draw!")
                return True


player = "x"
game_on = True

screen.fill((255, 255, 255))
while True:
    screen.blit(bg, (0, 0))
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

                else:
                    if player == "x":
                        player = "o"
                    else:
                        player = "x"

    for i, x in enumerate(array):
        if array[i] == 'x':
            screen.blit(img_x, (coordinates[i][0], coordinates[i][1]))
        elif array[i] == "o":
            screen.blit(img_o, (coordinates[i][0], coordinates[i][1]))

    pygame.display.update()

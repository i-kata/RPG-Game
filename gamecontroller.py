from window import Window
from square import Square
import pygame
import sys


class GameController:

    def __init__(self):
        self.window = Window(1280, 720)

    def print_gameboard(self):  # method to randomize non-player objects spawning
        for row in range(len(self.window.gameboard)):
            for col in range(len(self.window.gameboard)):
                print(self.window.gameboard[row][col], end='')
            print()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for x in range(len(self.window.pos_color_array)):
                print("POS TUPPLE: " + str(self.window.pos_color_array[x][0]))
                print("COL TUPPLE: " + str(self.window.pos_color_array[x][1]))

            pygame.display.update()

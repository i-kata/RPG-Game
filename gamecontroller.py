from window import Window
from gameboard import GameBoard
from square import Square
import pygame
import sys


class GameController(GameBoard):

    def __init__(self):
        super().__init__()
        self.window = Window(1280, 720)

    def print_gameboard(self):
        for row in range(len(self.gameboard)):
            for col in range(len(self.gameboard)):
                print(self.gameboard[row][col], end='')
            print()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for pos in range(len(self.pos_color_list)):
                pygame.draw.rect(self.window.screen,
                                 self.pos_color_list[pos].color_tuple,
                                 [
                                     self.pos_color_list[pos].posx,
                                     self.pos_color_list[pos].posy,
                                     Square.width,
                                     Square.height
                                 ])

            self.pos_color_list[0].move()

            pygame.display.update()

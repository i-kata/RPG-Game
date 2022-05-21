import pygame
from gameboard import GameBoard


class Window(GameBoard):

    def __init__(self, height, width):
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Game")
        self.screen = pygame.display.set_mode((height, width))
        self.clock = pygame.time.Clock()

    def create_board(self):
        for row in range(len(self.gameMap)):
            for col in range(len(self.gameMap[row])):
                if self.gameMap[row][col] == 'x':
                    pass
                elif self.gameMap[row][col] == 'p':
                    pass
                else:
                    pass

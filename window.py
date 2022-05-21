import pygame
from gameboard import GameBoard


class Window(GameBoard):

    def __init__(self, height, width):
        super().__init__()
        pygame.init()
        pygame.display.set_caption("Game")
        self.screen = pygame.display.set_mode((height, width))
        self.clock = pygame.time.Clock()


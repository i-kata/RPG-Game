from window import Window
import pygame
import sys

class GameController:

    def __init__(self):
        self.window = Window(1280, 720)

    def gameMap_randomize(self):  # method to randomize non-player objects spawning
        for row in range(len(self.window.gameMap)):
            for col in range(len(self.window.gameMap)):
                print(self.window.gameMap[row][col], end='')
            print()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.window.screen.fill('black')
            pygame.draw.rect(self.window.screen, (255, 0, 200), (50, 50, 100, 100))

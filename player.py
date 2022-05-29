import pygame
from square import Square


class Player(Square):

    movement_speed: float = 5
    possible_directions: dict = {'Right': 1, 'Left': -1, 'Top': -1, 'Bottom': 1}
    direction: int = 0

    def __init__(self, posx, posy, color_tuple):
        super().__init__(posx, posy, color_tuple)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = self.possible_directions['Top']
            self.posy = self.posy*self.height + self.movement_speed*self.direction
            print(self.direction + self.posy)

        if keys[pygame.K_DOWN]:
            self.direction = self.possible_directions['Bottom']
            self.posy = self.posy*self.height + self.movement_speed*self.direction
            print(self.direction + self.posy)

        if keys[pygame.K_RIGHT]:
            self.direction = self.possible_directions['Right']
            self.posx = self.posx*self.width + self.movement_speed*self.direction
            print(self.direction + self.posx)

        if keys[pygame.K_LEFT]:
            self.direction = self.possible_directions['Left']
            self.posx = self.posx*self.width + self.movement_speed*self.direction
            print(self.direction + self.posx)

    def detect_collision(self):
        pass
import pygame

from square import Square


class Player(Square):

    movement_speed: float = 0
    direction: list = ['Right', 'Left', 'Top', 'Bottom']

    def __init__(self, posx, posy, color_tuple):
        super().__init__(posx, posy, color_tuple)

    def move(self):
        pass

    def detect_collision(self):
        pass


class Square:

    width = 64
    height = 64

    def __init__(self, posx: int, posy: int, color_tuple: tuple):
        self.posx = posx
        self.posy = posy
        self.color_tuple = color_tuple
from gameboard import GameBoard


class GameController:

    def __init__(self):
        self.gameboard = GameBoard

    def gameMap_randomize(self):  # method to randomize non-player objects spawning
        for row in range(len(self.gameboard.__init__().gameMap)):
            for col in range(len(GameBoard.__init__().gameMap)):
                pass
from gameboard import GameBoard


class GameController:

    def __init__(self):
        self.gameboard = GameBoard()

    def gameMap_randomize(self):  # method to randomize non-player objects spawning
        for row in range(len(self.gameboard.gameMap)):
            for col in range(len(self.gameboard.gameMap)):
                print(self.gameboard.gameMap[row][col], end='')
            print()

from gamecontroller import *
from gameboard import *

gamecontroller = GameController()
gameboard = GameBoard()
gamecontroller.print_gameboard()
gameboard.gen_pos_color_array()
gamecontroller.run_game()

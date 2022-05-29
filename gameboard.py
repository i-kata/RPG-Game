from square import Square


class GameBoard:

    def __init__(self):
        self.gameboard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ]

        self.pos_color_list: list[Square] = []


    def gen_pos_color_list(self):

        for row in range(len(self.gameboard)):
            for col in range(len(self.gameboard[row])):

                if self.gameboard[row][col] == 'x':
                    self.pos_color_list.append(Square(posx=Square.width*col,
                                                      posy=Square.height*row,
                                                      color_tuple=(255, 50, 0)))

                elif self.gameboard[row][col] == ' ':
                    self.pos_color_list.append(Square(posx=Square.width*col,
                                                      posy=Square.height*row,
                                                      color_tuple=(255, 150, 0)))

                else:
                    self.pos_color_list.append(Square(posx=Square.width*col,
                                                      posy=Square.height*row,
                                                      color_tuple=(255, 100, 0)))

    def print_pos_color_list(self):
        for pos in range(len(self.pos_color_list)):
            print("Square nr: " + str(pos) + "\n" +
                  "\t" + "posx: " + str(self.pos_color_list[pos].posx) +
                  "\t" + "posy: " + str(self.pos_color_list[pos].posy) +
                  "\t" + "color_tuple: " + str(self.pos_color_list[pos].color_tuple))

# for row in range(len(gameboard)):
#    for col in range(len(gameboard[row])):
#        if 0 < row < 19:
#            if col > 0 and col < 19:
#                if gameboard[row][col] == 'x':
#                    gameboard[row][col] = ' '
#
#
# for row in range(len(gameboard)):
#    print('[', end='')
#    for col in range(len(gameboard[row])):
#        if col < 19:
#            print("'" + gameboard[row][col] + "'", end=', ')
#        else:
#            print("'" + gameboard[row][col] + "'", end='')
#    print('],')

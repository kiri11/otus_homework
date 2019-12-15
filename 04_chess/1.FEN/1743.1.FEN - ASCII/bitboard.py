class Board:
    def __init__(self, fen):
        self.fen = fen.split('/')

    def __str__(self):
        res = "  +-----------------+\n"
        for i, line in zip(range(8, 0, -1), self.fen):
            res += "%i | " % i
            for char in line:
                if char.isdigit():
                    res += '. ' * int(char)
                else:
                    res += char + ' '
            res += '|\n'
        return res + "  +-----------------+\n    a b c d e f g h"

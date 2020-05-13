class King:
    nA = 0xFeFeFeFeFeFeFeFe
    nH = 0x7f7f7f7f7f7f7f7f
    fullBoard = 0xffffffffffffffff

    def __init__(self, position):
        self.position = 1 << position

    def valid_moves(self):
        return ((self.position << 8 | self.position >> 8)
                | self.nH & (self.position >> 9 | self.position >> 1 | self.position << 7)
                | self.nA & (self.position >> 7 | self.position << 1 | self.position << 9)) \
                & self.fullBoard

    def __str__(self):
        return "\n".join(str(getattr(self, figure)) for figure in "PNBRQKpnbrqk")


def setbitcount(num):
    """Calculate number of set bits in a positive int number"""
    return bin(num).count('1')


def king_solver(input_txt):
    n = King(int(input_txt.strip()))
    moves = n.valid_moves()
    moves_count = setbitcount(moves)
    return "%s\n%s" % (moves_count, moves)


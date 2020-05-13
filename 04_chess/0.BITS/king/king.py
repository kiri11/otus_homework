from tester import check_chess_class


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


if __name__ == "__main__":
    check_chess_class(King)

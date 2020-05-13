from tester import check_chess_class


class Knight:
    nA = 0xFeFeFeFeFeFeFeFe
    nAB = 0xFcFcFcFcFcFcFcFc
    nH = 0x7f7f7f7f7f7f7f7f
    nGH = 0x3f3f3f3f3f3f3f3f

    def __init__(self, position):
        self.position = 1 << position

    def valid_moves(self):
        return self.nGH & (self.position << 6 | self.position >> 10)\
             | self.nH & (self.position << 15 | self.position >> 17)\
             | self.nA & (self.position << 17 | self.position >> 15)\
             | self.nAB & (self.position << 10 | self.position >> 6)

    def __str__(self):
        return "\n".join(str(getattr(self, figure)) for figure in "PNBRQKpnbrqk")


if __name__ == "__main__":
    check_chess_class(Knight)

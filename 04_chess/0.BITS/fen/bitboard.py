from itertools import chain
from tester import run_tests


class Board:
    def __init__(self, fen):
        self.P = 0
        self.N = 0
        self.B = 0
        self.R = 0
        self.Q = 0
        self.K = 0

        self.p = 0
        self.n = 0
        self.b = 0
        self.r = 0
        self.q = 0
        self.k = 0
        self.parse_fen(fen)

    def parse_fen(self, fen):
        bit = 1
        for char in chain.from_iterable(reversed(fen.split('/'))):
            if char.isdigit():
                bit <<= int(char)
            else:
                self.__dict__[char] += bit
                bit <<= 1

    def __str__(self):
        return "\n".join(str(getattr(self, figure)) for figure in "PNBRQKpnbrqk")


def board_reader(input_txt):
    b = Board(input_txt.strip())
    return str(b)


if __name__ == "__main__":
    run_tests(board_reader)

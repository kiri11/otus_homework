from abc import ABC, abstractmethod


class Figure(ABC):
    nA = 0xFeFeFeFeFeFeFeFe
    nAB = 0xFcFcFcFcFcFcFcFc
    nH = 0x7f7f7f7f7f7f7f7f
    nGH = 0x3f3f3f3f3f3f3f3f
    fullBoard = 0xffffffffffffffff

    def __init__(self, position):
        self.position = 1 << position

    @abstractmethod
    def valid_moves(self):
        ...

    def __str__(self):
        return "\n".join(str(getattr(self, figure)) for figure in "PNBRQKpnbrqk")


class Rook(Figure):
    ...


class Bishop(Figure):
    ...


class Queen(Rook, Bishop):
    ...


if __name__ == "__main__":
    ...

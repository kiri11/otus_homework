from fast_power import binary_power


def fib_rec(n):
    """Recursion algorithm. O(2^n)"""
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_n(n):
    """Classic iterative algorithm. O(n)"""
    if n == 0:
        return 0
    a = 0
    b = 1
    c = 1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c


class Matrix:
    """2x2 matrix."""

    @classmethod
    def IDENTITY(cls):
        return cls(1, 0, 0, 1)

    def __init__(self, a, b, c, d):
        self.mx = [a, b, c, d]

    def __imul__(self, other):
        self.mx = [self.mx[0] * other.mx[0] + self.mx[1] * other.mx[2],
                   self.mx[0] * other.mx[1] + self.mx[1] * other.mx[3],
                   self.mx[2] * other.mx[0] + self.mx[3] * other.mx[2],
                   self.mx[2] * other.mx[1] + self.mx[3] * other.mx[3]]
        return self

    def __pow__(self, power: int):
        return binary_power(self, power, self.IDENTITY())

    def __str__(self):
        return "|%s %s|\n|%s %s|" % tuple(self.mx)


def fib_matrix(n):
    """Using matrix. O(log(n))."""
    fibn_matrix = Matrix(0, 1, 1, 1) ** n
    return fibn_matrix.mx[2]


if __name__ == "__main__":
    assert fib_n(1) == fib_matrix(1) == fib_rec(1)
    print(fib_matrix(1))
    assert fib_n(10) == fib_matrix(10) == fib_rec(10)
    print(fib_matrix(10))
    assert fib_n(100) == fib_matrix(100)
    print(fib_matrix(100))
    assert fib_n(1000) == fib_matrix(1000)
    print(fib_matrix(1000))

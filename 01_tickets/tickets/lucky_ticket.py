from functools import lru_cache
from test import run_tests


@lru_cache
def p(m, s):
    """Кол-во m-значных чисел, сумма цифр каждого из которых равна s."""
    if s < 0 or s > 9*m:
        return 0
    if s == 0 or m == 1:
        return 1
    return p(m, s+1) - p(m-1, s+1) + p(m-1, s-9)


def lucky_count(n):
    """
    Билет с 2N значным номером считается счастливым,
    если сумма N первых цифр равна сумме последних N цифр.
    :return: количество 2N-значных счастливых билетов
    Идея: http://kvant.mccme.ru/1978/11/integralom_-_po_schastlivym_bi.htm
    """
    return p(2*n, 9*n)


def solve(inp):
    return lucky_count(int(inp))


if __name__ == "__main__":
    run_tests(solve)

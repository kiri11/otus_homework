from pathlib import Path
from knight import Knight


def check_func(func, in_file):
    test_name = in_file.name[:-3]
    out_filename = test_name + ".out"
    with in_file.open('r') as in_file:
        actual = func(in_file.read().strip())
        with open(out_filename, 'r') as out_file:
            expected = out_file.read().strip()
            if str(actual) == expected:
                print("%s pass" % test_name)
            else:
                print("%s fail.\nExpected:\n%s\nActual:\n%s" % (test_name, expected, actual))


def setbitcount(num):
    """Calculate number of set bits in a positive int number"""
    return sum(int(bit) for bit in bin(num)[2:])


def knight_solver(input_txt):
    n = Knight(int(input_txt.strip()))
    moves = n.valid_moves()
    moves_count = setbitcount(moves)
    return "%s\n%s" % (moves_count, moves)


def run_tests(folder='.'):
    for path in Path(folder).glob('test*.in'):
        check_func(knight_solver, path)


if __name__ == "__main__":
    run_tests()

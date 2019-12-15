from pathlib import Path
from bitboard import Board


def check_func(func, in_file):
    test_name = in_file.name[:-3]
    out_filename = test_name + ".out"
    with in_file.open('r') as in_file:
        actual = func(in_file.read().strip())
        with open(out_filename, 'r') as out_file:
            expected = out_file.read()
            if str(actual) == expected:
                print("%s pass" % test_name)
            else:
                print("%s fail.\nExpected:\n%s\nActual:\n%s" % (test_name, expected, actual))


def board_reader(input_txt):
    b = Board(input_txt.split(' ')[0])
    return str(b)


def run_tests(folder='.'):
    for path in Path(folder).glob('test*.in'):
        check_func(board_reader, path)


if __name__ == "__main__":
    run_tests()

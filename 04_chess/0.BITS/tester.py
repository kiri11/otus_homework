from pathlib import Path


def check_func(func, in_file, strip_expected=True):
    test_name = in_file.name[:-3]
    out_filename = test_name + ".out"
    with in_file.open('r') as in_file:
        actual = func(in_file.read().strip())
        with open(out_filename, 'r') as out_file:
            expected = out_file.read()
            if strip_expected:
                expected = expected.strip()
            if str(actual) == expected:
                print("%s pass" % test_name)
            else:
                print("%s fail.\nExpected:\n%s\nActual:\n%s" % (test_name, expected, actual))


def run_tests(func, folder='.'):
    for path in Path(folder).glob('test*.in'):
        check_func(func, path)


def setbitcount(num):
    """Calculate number of set bits in a positive int number"""
    return bin(num).count('1')


def solver(figure_class):
    def solver_func(input_txt):
        n = figure_class(int(input_txt.strip()))
        moves = n.valid_moves()
        moves_count = setbitcount(moves)
        return "%s\n%s" % (moves_count, moves)
    return solver_func


def check_chess_class(chess_class):
    run_tests(solver(chess_class))

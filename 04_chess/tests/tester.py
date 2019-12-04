from pathlib import Path


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
                print("%s fail. Expected: %s. Actual: %s " % (test_name, expected, actual))


def run_tests(folder='.'):
    for path in Path(folder).glob('test*.in'):
        check_func(len, path)


if __name__ == "__main__":
    run_tests()

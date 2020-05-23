from pathlib import Path


def check_func(func, in_path, strip_expected=True):
    test_name = in_path
    with in_path.open('r') as in_file:
        actual = func(in_file.read().strip())
        out_filename = in_path.with_suffix(".out")
        with open(out_filename, 'r') as out_file:
            expected = out_file.read()
            if strip_expected:
                expected = expected.strip()
            if str(actual) == expected:
                print("%s pass" % test_name)
            else:
                print("%s fail.\nExpected:\n%s\nActual:\n%s" % (test_name, expected, actual))


def run_tests(func, decorator=lambda x: x, folder='.'):
    for path in Path(folder).rglob('test*.in'):
        check_func(decorator(func), path)

from collections import Counter
from operator import itemgetter
from timeit import timeit
from bin_num_file import read_bin_file


def counting_sort_arbitrary_keys(arr):
    pairs = sorted(Counter(arr).items(), key=itemgetter(0))
    res = []
    for i, c in pairs:
        for _ in range(c):
            res.append(i)
    return res


def counting_sort_unsigned_shorts(arr):
    counter = [0] * 65536
    for x in arr:
        counter[x] += 1
    print("read file finished")
    for i, c in enumerate(counter):
        for _ in range(c):
            yield i


def main():
    def run_sort():
        nonlocal out
        out = counting_sort_arbitrary_keys(arr)
        return list(out)

    for i in [5, 6, 7, 8, 9]:
        with open('test%i.bin' % i, 'rb') as inp:
            arr = read_bin_file(inp)
            out = None
            running_time = timeit(run_sort, number=1, globals=locals())
        print("10^%i\t%fs" % (i, running_time))


if __name__ == "__main__":
    main()

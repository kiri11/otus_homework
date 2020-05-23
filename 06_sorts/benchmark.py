from timeit import timeit


def bench_array(func):
    def bench_func(input_txt):
        ln, str_arr = input_txt.split('\n')
        arr = list(map(int, str_arr.split()))
        running_time = timeit(lambda: func(arr), number=1, globals=locals())
        print("%i\t%fs\t" % (len(arr), running_time), end=' ')
        res = ' '.join(map(str, arr))
        return res
    return bench_func

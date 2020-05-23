from tester import run_tests
from benchmark import bench_array


def classic_shell(n):
    while n > 0:
        n //= 2
        yield n


ci01 = [701, 301, 132, 57, 23, 10, 4, 1]


def shell_sort_1(array):
    increment = len(array) // 2
    while increment > 0:

        for startPosition in range(increment):
            gap_insertion_sort(array, startPosition, increment)

        increment //= 2


def gap_insertion_sort(array, low, gap):
    for i in range(low + gap, len(array), gap):
        currentvalue = array[i]
        position = i

        while position >= gap and array[position - gap] > currentvalue:
            array[position] = array[position - gap]
            position = position - gap

        array[position] = currentvalue


def shell_sort(gaps):
    def shell_sort_partial(a):
        n = len(a)
        for gap in gaps(n):
            # Do a gapped insertion sort for this gap size.
            # The first gap elements a[0..gap-1] are already in gapped order
            # keep adding one more element until the entire array is gap sorted
            for i in range(gap, n):
                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = a[i]
                # shift earlier gap-sorted elements up until the correct location for a[i] is found
                j = i
                while j >= gap and a[j - gap] > temp:
                    a[j] = a[j - gap]
                    j -= gap
                # put temp (the original a[i]) in its correct location
                a[j] = temp
    return shell_sort_partial


if __name__ == "__main__":
    run_tests(shell_sort(classic_shell), bench_array, "tests/random")

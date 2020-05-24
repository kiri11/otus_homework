from tester import run_tests
from benchmark import bench_array
from math import floor


def classic_shell(n):
    # Original Shell gap sequence, 1959, O(N^2) worst case
    while n > 0:
        n //= 2
        yield n


def ps65(n):
    # Papernov & Stasevich, 1965, O(N^(3/2)) worst case
    seq = [1]
    k = 1
    elem = 2
    while elem < n:
        seq.append(elem)
        elem = 2 ** k + 1
        k += 1
    return reversed(seq)


def ci_01(n):
    # Optimal (best known) sequence of increments for shell sort algorithm.
    ci01 = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
    # Extend the sequence
    while ci01[-1] < n:
        ci01.append(floor(2.25*ci01[-1]))
    return reversed(ci01)


def shell_sort_partial(gaps):
    def shell_sort(a):
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
    return shell_sort


if __name__ == "__main__":
    for gap_sequence in (classic_shell, ps65, ci_01):
        for test_type in ("random", "digits", "sorted", "revers"):
            run_tests(shell_sort_partial(gap_sequence), bench_array, "tests/" + test_type)

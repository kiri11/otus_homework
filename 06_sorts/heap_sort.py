from tester import run_tests
from benchmark import bench_array


def heap_sort(arr):
    def down(root, size):
        l = 2 * root + 1
        r = l + 1

        # x = max(l, r, root)
        x = root
        if l < size and arr[l] > arr[x]:
            x = l
        if r < size and arr[r] > arr[x]:
            x = r

        if x != root:
            arr[x], arr[root] = arr[root], arr[x]
            down(x, size)

    n = len(arr)
    # heapify
    for i in reversed(range(n // 2)):
        down(i, n)

    for i in reversed(range(n)):
        arr[0], arr[i] = arr[i], arr[0]
        down(0, i)

    return arr


if __name__ == "__main__":
    for test_type in ("random", "digits", "sorted", "revers"):
        run_tests(heap_sort, bench_array, "tests/" + test_type)

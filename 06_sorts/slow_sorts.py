from tester import run_tests
from benchmark import bench_array


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        # пока j > 0 и элемент j-1 > j
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j-1]
            else:
                break


if __name__ == "__main__":
    for test_type in ("random", "digits", "sorted", "revers"):
        run_tests(insertion_sort, bench_array, "five/" + test_type)

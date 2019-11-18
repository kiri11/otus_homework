from timeit import timeit
from dynamic_arrays import SingleArray

METHODS = {
    "insert at the end": "insert(len(arr), 1)",
    "insert at the beginning": "insert(0, 1)",
    "insert at random": "insert(randint(0, len(arr)), 1)"
}


def test_add_array(arr_cls, tries: int) -> None:
    for method_name, method in METHODS.items():
        from random import randint
        average = timeit("arr.%s" % method, "arr = arr_cls()", number=tries, globals=locals())

        print("%s.%s: %fms." % (arr_cls.__name__, method_name, average * tries))


if __name__ == "__main__":
    test_add_array(SingleArray, 10000)

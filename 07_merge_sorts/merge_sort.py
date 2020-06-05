def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a = merge_sort(arr[mid:])
    b = merge_sort(arr[:mid])
    return merge(a, b)


def merge(a, b):
    """Merge two sorted arrays into one, maintaining sorting."""
    res = []
    pa = 0
    pb = 0
    while pa < len(a) and pb < len(b):
        if a[pa] < b[pb]:
            res.append(a[pa])
            pa += 1
        else:
            res.append(b[pb])
            pb += 1
    while pa < len(a):
        res.append(a[pa])
        pa += 1
    while pb < len(b):
        res.append(b[pb])
        pb += 1

    return res


print(merge([1, 2, 3, 4, 7, 8, 110], [0, 2, 5, 6, 9, 16]))
print(merge_sort([3, 45, 1, 4, 7, 0]))

import struct
from timeit import timeit
from tempfile import TemporaryFile
from bin_num_file import read_bin_file_in_full, pack_format, SIZEOF_NUM

CHUNK_SIZE = 2**28


def write_to_temp(arr):
    packed = struct.pack(pack_format(len(arr)), *arr)
    res_file = TemporaryFile(mode='r+b')
    res_file.write(packed)
    res_file.seek(0)
    print("Wrote chunk of size %i bytes" % len(packed))
    return res_file


def merge_file_sort(file, left=0, right=None):
    if right is None:
        file.seek(0, 2)
        right = file.tell() // SIZEOF_NUM
        file.seek(0)
    size = (right - left)
    if size <= CHUNK_SIZE:
        file.seek(left * SIZEOF_NUM)
        file_part = file.read(SIZEOF_NUM * size)
        res = struct.unpack(pack_format(size), file_part)
        return write_to_temp(sorted(res))
    mid = (left + right) // 2
    a = merge_file_sort(file, left, mid)
    b = merge_file_sort(file, mid, right)
    merged = merge(a, b)
    print("merged")
    a.close()
    b.close()
    return merged


def merge(file_a, file_b):
    """Merge two sorted files into one, maintaining sorting."""
    print("merge started")
    res = []
    a = read_bin_file_in_full(file_a)
    b = read_bin_file_in_full(file_b)
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

    return write_to_temp(res)


def main():
    def run_merge():
        nonlocal out
        out = merge_file_sort(inp)
        return out

    for i in [5, 6, 7, 8, 9]:
        with open('test%i.bin' % i, 'rb') as inp:
            out = None
            running_time = timeit(run_merge, number=1, globals=locals())
            print("10^%i\t%fs" % (i, running_time))


if __name__ == "__main__":
    main()

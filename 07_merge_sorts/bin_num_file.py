import random
import struct

SIZEOF_NUM = 2  # in bytes
MEMORY_LIMIT = 10 ** 8


def gen_nums(length, max_size=65535):
    return (random.randint(0, max_size) for _ in range(0, length))


def pack_format(n):
    """Struct of exactly n of unsigned short (2 bytes)"""
    return "%iH" % n


def generate_test_file(filename, length_power):
    length = 10 ** length_power
    left_to_write = length
    with open(filename, 'wb') as file:
        while left_to_write > 0:
            cur_len = min(left_to_write, MEMORY_LIMIT)
            packed = struct.pack(pack_format(cur_len), *gen_nums(cur_len))
            file.write(packed)
            left_to_write -= cur_len
            print("Left to write %i bytes" % left_to_write)
    print("Generated 10^%i numbers and saved in binary file %s" % (length_power, filename))


def read_bin_file(f, chunk_size_int=10**8):
    chunk_size_byte = chunk_size_int * 2
    while True:
        packed = f.read(chunk_size_byte)
        packed_length = len(packed) // SIZEOF_NUM
        if not packed:
            break
        yield from struct.unpack(pack_format(min(chunk_size_int, packed_length)), packed)


def read_bin_file_in_full(file):
    packed = file.read()
    length = len(packed) // SIZEOF_NUM
    return struct.unpack(pack_format(length), packed)


if __name__ == "__main__":
    for length_power in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        filename = 'test%i.bin' % length_power
        generate_test_file(filename, length_power)

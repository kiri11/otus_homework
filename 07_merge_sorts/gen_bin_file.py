import random
import struct


def gen_nums(length, max_size=65535):
    return (random.randint(0, max_size) for _ in range(0, length))


def pack_format(n):
    """Struct of exactly n of unsigned short (2 bytes)"""
    return "%iH" % n


def generate_test_file(filename, length_power):
    length = 10 ** length_power
    packed = struct.pack(pack_format(length), *gen_nums(length))
    with open(filename, 'wb') as file:
        file.write(packed)
    print("Generated 10^%i numbers and saved in binary file %s" % (length_power, filename))


def read_test_file(filename):
    with open(filename, 'rb') as file:
        packed = file.read()
    sizeof_num = 2  # in bytes
    length = len(packed) // sizeof_num
    return struct.unpack(pack_format(length), packed)


if __name__ == "__main__":
    length_power = 1
    filename = 'test%i.bin' % length_power
    generate_test_file(filename, length_power)
    print(read_test_file(filename))

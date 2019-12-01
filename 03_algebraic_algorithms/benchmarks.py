from timeit import timeit
from fast_power import binary_power, two_step, mult_power
from fibonacci import fib_rec, fib_n, fib_matrix

tests = [
    (100, 100),
    (2, 1024),
    (3, 1024),
    (300, 1024),
    (2, 873459),
    (5, 873459),
]


def bench_power(tries: int) -> None:
    for base, power in tests:
        builtin = "%i ** %i" % (base, power)
        builtin_time = timeit(builtin, number=tries)
        custom_time = timeit("binary_power(%i, %i)" % (base, power), number=tries, globals=globals())
        two_step_time = timeit("two_step(%i, %i)" % (base, power), number=tries, globals=globals())
        mult_time = timeit("mult_power(%i, %i)" % (base, power), number=tries, globals=globals())

        print("%s\tBuilt-in: %fs. Binary: %fs. Two-step: %fs. Multiplication: %fs." %
              (builtin, builtin_time, custom_time, two_step_time, mult_time))


def bench_fibo(tries: int) -> None:
    for n in (10, 30, 35, 36):
        fib_rec_time = timeit("fib_rec(%i)" % n, number=tries, globals=globals())
        fib_n_time = timeit("fib_n(%i)" % n, number=tries, globals=globals())
        fib_matrix_time = timeit("fib_matrix(%i)" % n, number=tries, globals=globals())

        print("N=%i\t\tRecursion: %fs. Dynamic: %fs. Matrix: %fs." %
              (n, fib_rec_time, fib_n_time, fib_matrix_time))

    for n in (100, 1000, 10000, 100000, 1000000):
        fib_n_time = timeit("fib_n(%i)" % n, number=tries, globals=globals())
        fib_matrix_time = timeit("fib_matrix(%i)" % n, number=tries, globals=globals())

        print("N=%i\t\tDynamic: %fs. Matrix: %fs." %
              (n, fib_n_time, fib_matrix_time))


if __name__ == "__main__":
    print("Exponentiation Algorithms:")
    bench_power(1)
    print()
    print("Fibonacci Algorithms:")
    bench_fibo(1)

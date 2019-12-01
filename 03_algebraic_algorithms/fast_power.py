def mult_power(base, power):
    """Plain multiplication"""
    res = 1
    for _ in range(power):
        res *= base
    return res


def two_step(base, power):
    """First 2^k, then just multiplication."""
    if power == 0:
        return 1
    res = base
    k = 1
    while k < power / 2:
        k *= 2
        res *= res
    while k < power:
        k += 1
        res *= base
    return res


def binary_power(base, power, init=1):
    """Left to right method"""
    while power:
        if power % 2:
            init *= base
        base *= base
        power //= 2
    return init


if __name__ == "__main__":
    assert (mult_power(3, 10)) == 3 ** 10
    assert (mult_power(30, 10)) == 30 ** 10
    assert (binary_power(1, 10)) == 1 ** 10
    assert (binary_power(21, 13)) == 21 ** 13
    assert (two_step(3, 10)) == 3 ** 10
    assert (two_step(30, 10)) == 30 ** 10
    assert (two_step(1, 10)) == 1 ** 10
    assert (mult_power(21, 0)) == 21 ** 0
    assert (binary_power(21, 0)) == 21 ** 0
    assert (two_step(21, 0)) == 21 ** 0

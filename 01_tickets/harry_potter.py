from math import sin


def print_spell(i, spell, n):
    print("%i.jpg" % (i+1))
    for x in range(n):
        for y in range(n):
            print('#' if spell(x, y) else '.', end=' ')
        print()
    print()


def main(n=25):
    for i, spell in enumerate([
        lambda x, y: x < y,
        lambda x, y: x == y,
        lambda x, y: x + y == n - 1,
        lambda x, y: x + y < n + 5,
        lambda x, y: x - y // 2 == 0,
        lambda x, y: x < 10 or y < 10,
        lambda x, y: x > 15 and y > 15,
        lambda x, y: x * y == 0,
        lambda x, y: abs(x - y) > 10,
        lambda x, y: x <= y-1 <= 2*x,
        lambda x, y: x in {1, n - 2} or y in {1, n - 2},
        lambda x, y: x*x + y*y <= 400,
        lambda x, y: 20 <= x + y < 29,
        lambda x, y: (x - n) ** 2 + (y - n)**2 >= (n-4) ** 2,
        lambda x, y: 10 < abs(x - y) <= 20,
        lambda x, y: abs(x - 12) + abs(y-12) < 10,
        lambda x, y: x >= 9*sin(y/3) + 15,
    ]):
        print_spell(i, spell, n)


if __name__ == "__main__":
    main()

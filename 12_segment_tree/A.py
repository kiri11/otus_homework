# https://codeforces.com/gym/100249/attachments
from math import log2, ceil
from operator import add


class SegmentTree:
    def __init__(self, n, func=add):
        self.shift = 2 ** ceil(log2(n))
        self.tree = [0] * self.shift * 2
        self.func = func
        self.identity = 0

    def assign(self, i, x):
        i += self.shift
        self.tree[i] = x
        while i > 0:
            sibling = i - 1 if i % 2 else i + 1
            self.tree[i // 2] = self.func(self.tree[i], self.tree[sibling])
            i //= 2

    def calc(self, l, r):
        l += self.shift
        r += self.shift
        res = self.identity
        while l <= r:
            if l % 2:
                res = self.func(res, self.tree[l])
            l = (l + 1) // 2
            if r % 2 == 0:
                res = self.func(res, self.tree[r])
            r = (r - 1) // 2
        return res


def main():
    with open("sum.in", 'r') as inp:
        n, k = map(int, inp.readline().split())
        st = SegmentTree(n)
        res = []
        for _ in range(k):
            line = inp.readline()
            if line:
                if line[0] == 'A':
                    i, x = map(int, line.split()[1:])
                    st.assign(i-1, x)
                elif line[0] == 'Q':
                    l, r = map(int, line.split()[1:])
                    res.append(st.calc(l-1, r-1))
        with open("sum.out", 'w') as out:
            out.writelines("%i\n" % i for i in res)


main()

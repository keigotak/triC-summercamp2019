# https://onlinejudge.u-aizu.ac.jp/courses/library/6/NTL/1/NTL_1_B

m, n = [int(x) for x in input().split()]

mod = 10**9 + 7


def func(m, n):
    if n == 1:
        return m
    if n % 2 == 0:
        return int(func(m, n//2) ** 2) % mod
    else:
        return int(m * func(m, n-1)) % mod


if __name__ == "__main__":
    print(func(m, n))
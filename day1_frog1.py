# https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
h = [int(x) for x in input().split()]

dp = [10**9] * n
dp[0] = 0

memo = dict()


def func(n):
    # for i in range(n):
    #     if i+1 < n:
    #         memo[(i, i+1)] = abs(h[i] - h[i+1])
    #     if i+2 < n:
    #         memo[(i, i+2)] = abs(h[i] - h[i+2])
    for i in range(1, n):
        if i - 1 >= 0:
            dp[i] = min(dp[i], dp[i-1] + abs(h[i-1] - h[i]))
        if i - 2 >= 0:
            dp[i] = min(dp[i], dp[i-2] + abs(h[i-2] - h[i]))

    return dp[-1]


if __name__ == "__main__":
    print(func(n))
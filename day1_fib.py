n = int(input())


memo = [-1] * 100
memo[0] = 1
memo[1] = 1


def fib(n):
    if memo[n] != -1:
        return memo[n]
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


if __name__ == "__main__":
    print(fib(n))
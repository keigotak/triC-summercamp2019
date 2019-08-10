n = int(input())
stones = [int(input()) for _ in range(n)]

dp = ['L'] * 100
dp[0] = 'L'
dp[1] = 'L'
dp[2] = 'W'

for i in range(3, 100):
    flg = False
    for step in [2,3,5]:
        if i - step >= 0:
            if dp[i - step] == 'L':
                flg = True
                break
    if flg:
        dp[i] = 'W'

for stone in stones:
    if dp[stone] == 'W':
        print('First')
    else:
        print('Second')


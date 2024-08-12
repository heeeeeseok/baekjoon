MAX = 10001
dp = [0] * MAX
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, MAX):
    dp[i] = 1 + (i // 2) + (i // 3)
    if i == 5:
        dp[i] += 1
    elif i > 5:
        dp[i] += dp[i - 5]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])



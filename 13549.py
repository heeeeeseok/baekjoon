n, k = map(int, input().split())

dp = [abs(n - i) for i in range(100001)]
for i in range(1, 100000):
    dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1)
    cur = i * 2
    while cur <= 100000:
        dp[cur] = min(dp[cur], dp[i])
        cur *= 2
print(dp[k])

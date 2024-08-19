n, d = map(int, input().split())
dp = [i for i in range(d + 2)]
shortcuts = []
for _ in range(n):
    start, end, length = map(int, input().split())
    start = min(start, d + 1)
    end = min(end, d + 1)
    shortcuts.append([start, end, length])
for i in range(d + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for j in range(n):
        start, end, length = shortcuts[j]
        if end == i:
            dp[i] = min(dp[i], dp[start] + length)
print(dp[d])

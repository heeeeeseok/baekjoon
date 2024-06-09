n = int(input())
costs = []
for _ in range(n):
    r, g, b = map(int, input().split())
    costs.append([r, g, b])
answer = 210000000
for i in range(3):
    dp = [[10000001 for _ in range(3)] for _ in range(n)]
    dp[0][i] = costs[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + costs[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + costs[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + costs[j][2]
    for j in range(3):
        if i != j:
            answer = min(answer, dp[-1][j])
print(answer)


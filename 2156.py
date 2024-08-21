# 연속으로 놓인 3잔을 모두 마실 수는 없다
# 가장 많은 양의 포도주를 마실 수 있는 경우를 구한다
# 그리디 x

n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))

if n <= 2:
    print(sum(wines))
    exit()

dp = [[0] * 3 for _ in range(n)]
dp[0][1] = wines[0]
dp[1][0] = wines[0]
dp[1][1] = wines[1]
dp[1][2] = wines[0] + wines[1]
for i in range(2, n):
    dp[i][0] = max(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + wines[i]
    dp[i][2] = dp[i - 1][1] + wines[i]
print(max(dp[-1]))

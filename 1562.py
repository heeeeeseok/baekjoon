n = int(input())
# dp[i][j][k] : 길이가 (i + 1), 마지막 숫자가 j, 현재까지 사용한 숫자들의 비트 k (비트마스킹)
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n)]
for i in range(10):
    dp[0][i][1 << i] = 1
for i in range(1, n):
    for j in range(10):
        for k in range(1 << 10):
            if j == 0:
                dp[i][j][k | 1 << j] += dp[i - 1][j + 1][k]
                dp[i][j][k | 1 << j] %= 1000000000
            elif j == 9:
                dp[i][j][k | 1 << j] += dp[i - 1][j - 1][k]
                dp[i][j][k | 1 << j] %= 1000000000
            else:
                dp[i][j][k | 1 << j] += dp[i - 1][j - 1][k] + dp[i - 1][j + 1][k]
                dp[i][j][k | 1 << j] %= 1000000000
answer = 0
# 1~9가 모두 포함된 경우를 계산
for i in range(1, 10):
    answer += dp[n - 1][i][1023]
    answer %= 1000000000
print(answer)
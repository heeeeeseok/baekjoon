import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
dp[0][0] = board[0][0]
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + board[0][i]

# 위쪽으로는 이동할 수 없으므로 좌, 우로의 dp를 통해 최대값을 구한다
for i in range(1, n):
    for j in range(m):  # 아래로 한 칸 이동
        dp[i][j] = dp[i - 1][j] + board[i][j]
    right_dp = deepcopy(dp[i])
    for j in range(1, m):  # 오른쪽 방향 이동
        right_dp[j] = max(right_dp[j], right_dp[j - 1] + board[i][j])
    left_dp = deepcopy(dp[i])
    for j in range(m - 2, -1, -1):  # 왼쪽 방향 이동
        left_dp[j] = max(left_dp[j], left_dp[j + 1] + board[i][j])
    for j in range(m):  # 최대값 갱신
        dp[i][j] = max(dp[i][j], right_dp[j], left_dp[j])
print(dp[-1][-1])
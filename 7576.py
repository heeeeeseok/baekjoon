from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
# 열, 행
m, n = map(int, input().split())
board = []
dq = deque()
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] == 1:
            dq.append((i, j, 0))

answer = 0
while dq:
    y, x, cnt = dq.popleft()
    answer = max(answer, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
            dq.append((ny, nx, cnt + 1))
            board[ny][nx] = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 0이 있다면 실패
            print(-1)
            exit()
print(answer)

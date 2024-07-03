from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
board = [[0] * m for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        board[i][j] = int(row[j])
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
dq = deque()
dq.append((0, 0))
while dq:
    y, x = dq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
            dq.append((ny, nx))
            board[ny][nx] = board[y][x] + 1
print(board[n -1][m - 1])
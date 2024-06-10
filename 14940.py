from collections import deque


n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dest_pos = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        board[i][j] = row[j]
        if row[j] == 2:
            dest_pos = (i, j)
        if row[j] == 0:
            answer[i][j] = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer[dest_pos[0]][dest_pos[1]] = 0
dq = deque()
dq.append((dest_pos[0], dest_pos[1], 0))
while dq:
    y, x, length = dq.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
            if not visited[ny][nx]:
                visited[ny][nx] = 1
                answer[ny][nx] = length + 1
                dq.append((ny, nx, length + 1))
for row in answer:
    for elem in row:
        print(elem, end=" ")
    print()

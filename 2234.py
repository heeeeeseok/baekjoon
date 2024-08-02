from collections import deque

def bfs(y, x, cnt):
    global visited, area_dict
    visited[y][x] = cnt
    dq = deque([(i, j)])
    area = 1
    while dq:
        cy, cx = dq.popleft()
        # 서: 1
        if board[cy][cx] % 2 == 0:
            if cx - 1 >= 0 and not visited[cy][cx - 1]:
                dq.append((cy, cx - 1))
                visited[cy][cx - 1] = cnt
                area += 1
        # 북: 2
        if board[cy][cx] % 4 < 2:
            if cy - 1 >= 0 and not visited[cy - 1][cx]:
                dq.append((cy - 1, cx))
                visited[cy - 1][cx] = cnt
                area += 1
        # 동: 4
        if board[cy][cx] % 8 < 4:
            if cx + 1 < n and not visited[cy][cx + 1]:
                dq.append((cy, cx + 1))
                visited[cy][cx + 1] = cnt
                area += 1
        # 남: 8
        if board[cy][cx] % 16 < 8:
            if cy + 1 < m and not visited[cy + 1][cx]:
                dq.append((cy + 1, cx))
                visited[cy + 1][cx] = cnt
                area += 1
    area_dict[cnt] = area


n, m = map(int, input().split())
board = []
visited = [[0] * n for _ in range(m)]
area_dict = dict()  # 각 방의 크기
for _ in range(m):
    board.append(list(map(int, input().split())))

cnt = 1
max_area = -1
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, cnt)
            cnt += 1

cnt -= 1  # 마지막에 더해준 1 처리
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
max_two = -1
for y in range(m):
    for x in range(n):
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < m and 0 <= nx < n:
                # 인접한 곳이 다른 방이라면
                if visited[y][x] != visited[ny][nx]:
                    # 두 방의 크기를 더하고 max_two 갱신
                    max_two = max(max_two, area_dict[visited[y][x]] + area_dict[visited[ny][nx]])
print(cnt)
print(max(area_dict.values()))
print(max_two)


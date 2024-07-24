from collections import deque


r, c = map(int, input().split())
board = []
dq_j = deque()
dq_f = deque()
for i in range(r):
    board.append(list(input().rstrip()))
    for j in range(c):
        if board[i][j] == 'J':  # 지훈 위치
            dq_j.append((i, j))
        if board[i][j] == 'F':  # 불 위치
            dq_f.append((i, j))
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
answer = 0
while dq_j:  # 지훈이가 움질일 수 있다면 반복
    answer += 1

    # 불 BFS 1회
    next_fires = []
    while dq_f:
        y, x = dq_f.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] == '.' or board[ny][nx] == 'J':
                    board[ny][nx] = 'F'
                    next_fires.append((ny, nx))
    dq_f = deque(next_fires)

    # 지훈 BFS 1회
    next_jihoon = []
    while dq_j:
        y, x = dq_j.popleft()
        if y == 0 or y == r - 1 or x == 0 or x == c - 1:
            print(answer)
            exit()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if board[ny][nx] == '.':
                    board[ny][nx] = 'J'  # 방문처리
                    next_jihoon.append((ny, nx))
    dq_j = deque(next_jihoon)
print('IMPOSSIBLE')

from collections import deque
from copy import deepcopy


def is_zero():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                return False
    return True


def bfs():
    global visited
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                visited[i][j] = 1
                dq = deque()
                dq.append((i, j))
                while dq:
                    cur_y, cur_x = dq.popleft()
                    for i in range(4):
                        new_y = cur_y + dy[i]
                        new_x = cur_x + dx[i]
                        if 0 <= new_y < n and 0 <= new_x < m and board[new_y][new_x] != 0:
                            if not visited[new_y][new_x]:
                                visited[new_y][new_x] = 1
                                dq.append((new_y, new_x))
                return


n, m = map(int, input().split())
board = []
answer = 0
for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
while not is_zero():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    # bfs 1번 수행
    bfs()

    # 빙산이 나누어졌다면 종료
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                print(answer)
                exit()
    new_board = deepcopy(board)
    # 빙산 녹이기
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
                        if new_board[i][j] > 1:
                            new_board[i][j] -= 1
                        else:
                            new_board[i][j] = 0
    board = new_board
    answer += 1
print(0)

import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [[['O'] * c for _ in range(r)] for _ in range(5)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 0
for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == 'O':
            board[0][i][j] = 'O'
        else:
            board[0][i][j] = '.'

# 3
for y in range(r):
    for x in range(c):
        if board[0][y][x] == 'O':
            board[3][y][x] = '.'
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    board[3][ny][nx] = '.'

# 1
for y in range(r):
    for x in range(c):
        if board[3][y][x] == 'O':
            board[1][y][x] = '.'
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    board[1][ny][nx] = '.'

for y in range(r):
    for x in range(c):
        if n == 1:
            print(board[0][y][x], end='')
        elif n % 2 == 0:
            print(board[2][y][x], end='')
        else:
            print(board[n % 4][y][x], end='')
    print()

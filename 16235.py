import sys
from collections import deque
input = sys.stdin.readline


n, m, k = map(int, input().split())
board = [[5 for _ in range(n)] for _ in range(n)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [0, -1, 1, -1, 1, 0, -1, 1]

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    y, x, z = map(int, input().split())
    trees[y - 1][x - 1].append(z)

for _ in range(k):
    # 봄
    for y in range(n):
        for x in range(n):
            new_trees = deque()
            dead_trees_sum = 0
            for age in trees[y][x]:
                if board[y][x] >= age:
                    board[y][x] -= age
                    new_trees.append(age + 1)
                else:
                    dead_trees_sum += (age // 2)
            trees[y][x] = new_trees
            # 여름, 겨울
            board[y][x] += (dead_trees_sum + A[y][x])

    # 가을
    additional_trees = []
    for y in range(n):
        for x in range(n):
            for age in trees[y][x]:
                if age % 5 == 0:
                    for i in range(8):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < n and 0 <= nx < n:
                            additional_trees.append((ny, nx))
    for y, x in additional_trees:
        trees[y][x].appendleft(1)

answer = 0
for y in range(n):
    for x in range(n):
        answer += len(trees[y][x])
print(answer)



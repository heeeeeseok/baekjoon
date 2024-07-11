from collections import deque
import itertools
def is_adjacent(seven_pos):
    visited = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    dq = deque([seven_pos[0]])
    visited.append(seven_pos[0])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny, nx) in seven_pos and (ny, nx) not in visited:
                dq.append((ny, nx))
                visited.append((ny, nx))
    return len(visited) == 7


som_pos = []  # 이다솜파 위치
all_pos = []
for i in range(5):
    row = input()
    for j in range(5):
        all_pos.append((i, j))
        if row[j] == 'S':
            som_pos.append((i, j))

answer = 0
all_seven_pos = list(itertools.combinations(all_pos, 7))
for seven_pos in all_seven_pos:
    if is_adjacent(seven_pos):
        cnt = 0
        for pos in seven_pos:
            if pos in som_pos:
                cnt += 1
        if cnt >= 4:
            answer += 1
print(answer)



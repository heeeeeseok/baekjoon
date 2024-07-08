from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
chickens = []
houses = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 2:
            chickens.append((i, j))
        elif row[j] == 1:
            houses.append((i, j))

m_chickens = []
dq = deque()
for chicken in chickens:
    dq.append([chicken])
while dq:
    cur_chickens = dq.popleft()
    if len(cur_chickens) == m:
        m_chickens.append(cur_chickens)
        continue
    last_idx = chickens.index(cur_chickens[-1])
    for idx in range(last_idx + 1, len(chickens)):
        new_chickens = deepcopy(cur_chickens)
        if chickens[idx] not in cur_chickens:
            new_chickens.append(chickens[idx])
            dq.append(new_chickens)

chicken_dist = 987654321
for m_chicken in m_chickens:
    cur_sum = 0
    for house in houses:
        cur_min = 987654321
        for pos in m_chicken:
            cur_min = min(cur_min, abs(pos[0] - house[0]) + abs(pos[1] - house[1]))
        cur_sum += cur_min
    chicken_dist = min(chicken_dist, cur_sum)
print(chicken_dist)


import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
dq = deque()
edges = [[] for _ in range(n + 1)]
in_degree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    in_degree[b] += 1

answer = []
while len(answer) != n:
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            dq.append(i)
    while dq:
        idx = dq.popleft()
        for node in edges[idx]:
            in_degree[node] -= 1
        answer.append(idx)
        in_degree[idx] = -1

for idx in answer:
    print(idx, end=' ')

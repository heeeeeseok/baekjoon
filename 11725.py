from collections import deque

n = int(input())
edges = [[] for _ in range(n + 1)]
parents = dict()
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
visited = [0 for _ in range(n + 1)]
dq = deque()
dq.append(1)
while dq:
    cur_node = dq.pop()
    visited[cur_node] = 1
    for neighbor in edges[cur_node]:
        if not visited[neighbor]:
            dq.append(neighbor)
            parents[neighbor] = cur_node
for i in range(2, n + 1):
    print(parents[i])

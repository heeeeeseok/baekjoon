import heapq


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    INF = float('inf')
    weights = [INF] * (n + 1)
    weights[start] = 0
    while hq:
        weight, now = heapq.heappop(hq)
        if weight > weights[now]:
            continue
        for next, w in graph[now]:
            W = w + weight
            if weights[next] > W:
                weights[next] = W
                heapq.heappush(hq, (W, next))
    return weights


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])
start, end = map(int, input().split())
weights = dijkstra(start)
print(weights[end])

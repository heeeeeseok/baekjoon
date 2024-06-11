def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    global parent
    parent_a = find(a)
    parent_b = find(b)
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    roads.append((cost, a, b))

roads.sort()
parent = [i for i in range(n + 1)]
kruskal_result = []
for cost, a, b in roads:
    if len(kruskal_result) == n - 1:
        break
    if find(a) != find(b):
        union(a, b)
        kruskal_result.append(cost)
print(sum(kruskal_result) - max(kruskal_result))

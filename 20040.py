def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    global parent
    pa = find(a)
    pb = find(b)
    if pa != pb:
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb


def solve():
    for turn in range(1, m + 1):
        v1, v2 = map(int, input().split())
        if find(v1) == find(v2):
            print(turn)
            return
        union(v1, v2)
    print(0)


n, m = map(int, input().split())
parent = [i for i in range(n)]
solve()
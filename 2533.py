import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(node):
    visited[node] = 1
    dp[node][0] = 1
    for friend in edges[node]:
        if not visited[friend]:
            find(friend)  # dp[friend] 계산
            dp[node][1] += dp[friend][0]
            dp[node][0] += min(dp[friend][0], dp[friend][1])


n = int(input())
dp = [[0] * 2 for _ in range(n + 1)]  # 0: 얼리 어답터, 1: 아님
visited = [0] * (n + 1)
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
find(1)
print(min(dp[1][0], dp[1][1]))


def backtracking(cur, dist_sum):
    global answer
    if dist_sum > answer:
        return
    if len(visited) == n:
        answer = min(answer, dist_sum)
        return
    for i in range(len(dist[cur])):
        if i not in visited:
            visited.append(i)
            backtracking(i, dist_sum + dist[cur][i])
            visited.pop()


n, k = map(int, input().split())
dist = []
for _ in range(n):
    dist.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        for x in range(n):
            dist[i][j] = min(dist[i][j], dist[i][x] + dist[x][j])
visited = [k]
answer = 987654321
backtracking(k, 0)
print(answer)

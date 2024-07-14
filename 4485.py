import heapq

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

def dijkstra():
    global dist
    hq = []
    heapq.heappush(hq, (board[0][0], 0, 0))  # 현재 푸피가 작은 순
    while hq:
        lupy, y, x = heapq.heappop(hq)
        if y == n - 1 and x == n - 1:
            return dist[-1][-1]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                cur_dist = lupy + board[ny][nx]
                if cur_dist < dist[ny][nx]:  # 거리 갱신
                    dist[ny][nx] = cur_dist
                    heapq.heappush(hq, (cur_dist, ny, nx))


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))
    visited = [[0] * n for _ in range(n)]
    dist = [[987654321] * n for _ in range(n)]
    answer = dijkstra()
    print('Problem ' + str(cnt) + ': ' + str(answer))
    cnt += 1

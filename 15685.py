def dragon_curve(points:list):
    cur_idx = len(points) - 1
    last_idx = len(points) - 1
    while cur_idx >= 1:
        y_diff = points[cur_idx][0] - points[cur_idx - 1][0]
        x_diff = points[cur_idx][1] - points[cur_idx - 1][1]
        # 왼쪽
        if y_diff == 0 and x_diff == 1:
            # 위쪽
            points.append((points[last_idx][0] - 1, points[last_idx][1]))
        # 오른쪽
        elif y_diff == 0 and x_diff == -1:
            # 아래쪽
            points.append((points[last_idx][0] + 1, points[last_idx][1]))
        # 위쪽
        elif y_diff == 1 and x_diff == 0:
            # 오른쪽
            points.append((points[last_idx][0], points[last_idx][1] + 1))
        # 아래쪽
        elif y_diff == -1 and x_diff == 0:
            # 왼쪽
            points.append((points[last_idx][0], points[last_idx][1] - 1))
        cur_idx -= 1
        last_idx += 1
    return points


n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
# d: 오른쪽, 위쪽, 왼쪽, 아래쪽
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
total_points = set()
for _ in range(n):
    x, y, d, g = map(int, input().split())
    points = [(y, x)]
    points.append((y + dy[d], x + dx[d]))
    for i in range(g):
        points = dragon_curve(points)
    for point in points:
        if 0 <= point[0] < 101 and 0 <= point[1] < 101:
            total_points.add(point)
answer = 0
for i in range(100):
    for j in range(100):
        if (i, j) in total_points and \
                (i + 1, j) in total_points and \
                (i, j + 1) in total_points and \
                (i + 1, j + 1) in total_points:
            answer += 1
print(answer)

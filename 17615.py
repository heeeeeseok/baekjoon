n = int(input())
balls = [''] * n
row = input()
for i in range(n):
    balls[i] = row[i]

ball_groups = []
cur_color = balls[0]
cur_cnt = 1
for i in range(1, n):
    if balls[i] == cur_color:
        cur_cnt += 1
    else:
        ball_groups.append((cur_color, cur_cnt))
        cur_color = balls[i]
        cur_cnt = 1
ball_groups.append((cur_color, cur_cnt))

if len(ball_groups) <= 2:
    print(0)
    exit()

answer = 987654321

# 가장 왼쪽의 공에 있는 색갈과 같은 공들을 모두 왼쪽으로
cur_answer = 0
for i in range(2, len(ball_groups), 2):
    color, cnt = ball_groups[i]
    cur_answer += cnt
answer = min(answer, cur_answer)

# 가장 오른쪽에 있는 색갈과 같은 공들을 모두 오른쪽으로
cur_answer = 0
for i in range(len(ball_groups) - 3, -1, -2):
    color, cnt = ball_groups[i]
    cur_answer += cnt
answer = min(answer, cur_answer)

# 왼쪽에서 두 번째 그룹인 공들을 모두 왼쪽으로
cur_answer = 0
for i in range(1, len(ball_groups), 2):
    color, cnt = ball_groups[i]
    cur_answer += cnt
answer = min(answer, cur_answer)

# 오른쪽에서 두 번째 그룹인 공들을 모두 오른쪽으로
cur_answer = 0
for i in range(len(ball_groups) - 2, -1, -2):
    color, cnt = ball_groups[i]
    cur_answer += cnt
answer = min(answer, cur_answer)

print(answer)

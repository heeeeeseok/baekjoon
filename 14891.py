def rotate(gear_idx, dir):
    global gears
    gear = gears[gear_idx]
    new_gear = [0] * 8
    if dir == 1:  # 시계 방향
        for i in range(8):
            new_gear[i] = gear[(i - 1) % 8]
    else:  # 반시계 방향
        for i in range(8):
            new_gear[i] = gear[(i + 1) % 8]
    gears[gear_idx] = new_gear


gears = [[]]  # 1번부터 시작하기 위해 0번째에 빈 리스트 할당
for _ in range(4):
    gear = input()
    gear = [int(c) for c in gear]
    gears.append(gear)
k = int(input())
for _ in range(k):
    gear_idx, dir = map(int, input().split())
    rotate_gears = [(gear_idx, dir)]
    # 왼쪽 바퀴들 확인
    cur_idx = gear_idx
    cur_dir = dir
    while cur_idx > 1:
        # 극이 서로 다르다면 회전리스트에 포함
        if gears[cur_idx - 1][2] != gears[cur_idx][6]:
            rotate_gears.append((cur_idx - 1, cur_dir * -1))
            cur_idx = cur_idx - 1
            cur_dir = cur_dir * -1
        # 극이 서로 같다면 회전하지 않으므로 break
        else:
            break
    # 오른쪽 바퀴 확인
    cur_idx = gear_idx
    cur_dir = dir
    while cur_idx < 4:
        # 극이 서로 다르다면 회전리스트에 포함
        if gears[cur_idx][2] != gears[cur_idx + 1][6]:
            rotate_gears.append((cur_idx + 1, cur_dir * -1))
            cur_idx = cur_idx + 1
            cur_dir = cur_dir * -1
        # 극이 서로 같다면 회전하지 않으므로 break
        else:
            break
    # 회전
    for gear, dir in rotate_gears:
        rotate(gear, dir)
# 점수 계산
answer = 0
for i in range(1, 5):
    if gears[i][0] == 1:
        answer += (2 ** (i - 1))  # 1, 2, 4 ,8 점
print(answer)



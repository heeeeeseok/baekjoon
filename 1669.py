x, y = map(int, input().split())

# 키 차이가 2 이하인 경우 전처리
if y - x <= 2:
    print(y - x)
    exit()

# 각 날짜의 최대 키 차이를 구한다.
# 예) 5일: 1 2 3 2 1, 6일: 1 2 3 3 2 1
day = 3
day_sum = 4
while y - x > day_sum:
    day += 1
    if day % 2 == 0:
        day_sum += (day // 2)
    else:
        day_sum += (day // 2) + 1
print(day)

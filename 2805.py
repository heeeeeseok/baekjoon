import math

n, m = map(int, input().split())
heights = list(map(int, input().split()))
heights = sorted(heights, reverse=True)
answer = 0
left_m = m
for i in range(1, n):
    if (heights[i - 1] - heights[i]) * i < left_m:
        left_m -= (heights[i - 1] - heights[i]) * i
        answer += (heights[i - 1] - heights[i])
    else:
        answer += math.ceil(left_m / i)
        left_m = 0
        break
if left_m != 0:
    answer += math.ceil(left_m / n)
print(heights[0] - answer)

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# 숫자: 인덱스
num_dict = dict()
for i in range(n):
    num_dict[nums[i]] = i

answer = 0
for i in range(n):
    cur_num = nums[i]
    remain = x - cur_num
    # x에서 현재 수를 뺸 숫자가 존재하고 인덱스가 더 클 때
    if num_dict.get(remain, 0):
        if num_dict[remain] > i:
            answer += 1
print(answer)

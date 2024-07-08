import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
right = 0
answer = 1
cur_nums = dict()
while right < n:
    # 이미 해당 번호가 존재하는 경우
    if cur_nums.get(nums[right], 0):
        # 넣었을 때 k개 이하라면
        if cur_nums.get(nums[right]) + 1 <= k:
            cur_nums[nums[right]] += 1
            right += 1
            answer = max(answer, right - left)
        else:
            while nums[left] != nums[right]:
                cur_nums[nums[left]] -= 1
                left += 1
            cur_nums[nums[left]] -= 1
            left += 1
    # 해당 번호가 처음 등장하는 경우
    else:
        cur_nums[nums[right]] = 1
        right += 1
        answer = max(answer, right - left)
print(answer)



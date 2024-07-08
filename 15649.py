from collections import deque
from copy import deepcopy


n, m = map(int, input().split())
dq = deque()
for i in range(1, n + 1):
    dq.append([i])
while dq:
    nums = dq.popleft()
    if len(nums) == m:
        for num in nums:
            print(num, end=' ')
        print()
        continue
    for new_num in range(1, n + 1):
        nums_copy = deepcopy(nums)
        if new_num not in nums:
            nums_copy.append(new_num)
            dq.append(nums_copy)

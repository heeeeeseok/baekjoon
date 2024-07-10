from collections import deque
from copy import deepcopy

while True:
    row = list(map(int, input().split()))
    if row[0] == 0:
        break

    nums = row[1:]
    cases = []
    dq = deque()
    for i in range(len(nums) - 5):
        dq.append([nums[i]])
    while dq:
        cur_nums = dq.popleft()
        if len(cur_nums) == 6:
            cases.append(cur_nums)
            continue
        last_idx = nums.index(cur_nums[-1])
        for i in range(last_idx + 1, len(nums)):
            new_nums = deepcopy(cur_nums)
            if nums[i] not in cur_nums:
                new_nums.append(nums[i])
                dq.append(new_nums)
    for case in cases:
        for num in case:
            print(num, end=' ')
        print()
    print()
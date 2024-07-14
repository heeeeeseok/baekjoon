n = int(input())
nums = sorted(list(map(int, input().split())))
nums_dict = dict()
for num in nums:
    if nums_dict.get(num, 0):
        nums_dict[num] += 1
    else:
        nums_dict[num] = 1

answer = 0
visited = dict()
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        first = nums[i]
        second = nums[j]
        if visited.get(first + second, 1):
            nums_dict[first] -= 1
            nums_dict[second] -= 1
            if nums_dict.get(first + second, 0):  # 첫번째, 두번째 숫자를 더한 숫자가 존재한다면
                nums_dict[first] += 1
                nums_dict[second] += 1
                answer += nums_dict[first + second]  # 해당 숫자 개수만큼 더한다
                visited[first + second] = 0  # 방문처리
            else:
                nums_dict[first] += 1
                nums_dict[second] += 1
print(answer)
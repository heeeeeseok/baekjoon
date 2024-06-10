n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums_sum = dict()
nums_sum[0] = 0
for i in range(n):
    nums_sum[i + 1] = nums_sum[i] + nums[i]
for i in range(m):
    start, end = map(int, input().split())
    print(nums_sum[end] - nums_sum[start - 1])


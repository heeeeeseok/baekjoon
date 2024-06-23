import sys
input = sys.stdin.readline

n = int(input())
nums = [-1]  # 0번째 인덱스
nums.extend(list(map(int, input().split())))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
for i in range(1, n):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1
for k in range(2, n):
    for start in range(1, n - k + 1):
        end = start + k
        if nums[start] == nums[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start][end])


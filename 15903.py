import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))
hq = []
for num in nums:
    heapq.heappush(hq, num)

for i in range(m):
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)
    num_sum = num1 + num2
    heapq.heappush(hq, num_sum)
    heapq.heappush(hq, num_sum)

print(sum(hq))


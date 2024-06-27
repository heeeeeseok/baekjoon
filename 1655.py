import sys
import heapq
input = sys.stdin.readline


n = int(input())
mid = int(input())
print(mid)
max_pq = []
min_pq = []
for i in range(n - 1):
    cur_num = int(input())
    if cur_num <= mid:
        heapq.heappush(min_pq, -cur_num)
    else:
        heapq.heappush(max_pq, cur_num)
    total_len = len(min_pq) + 1 + len(max_pq)
    if total_len % 2 == 0:
        if len(min_pq) > len(max_pq):
            max_of_min = -heapq.heappop(min_pq)
            heapq.heappush(max_pq, mid)
            mid = max_of_min
    else:
        if len(min_pq) < len(max_pq):
            min_of_max = heapq.heappop(max_pq)
            heapq.heappush(min_pq, -mid)
            mid = min_of_max
    print(mid)
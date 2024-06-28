import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
board = []
for _ in range(n):
    board.append(int(input()))
answer = 1
for i in range(0, n + k - 1):
    cur = set()
    for x in range(k):
        cur.add(board[(i + x) % n])
    cur.add(c)
    answer = max(answer, len(cur))
print(answer)

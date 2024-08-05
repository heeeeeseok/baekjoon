from collections import deque


n = int(input())
buildings = list(map(int, input().split()))
answer = []
cur_list = []
dq = deque()

for i in range(len(buildings)):
    if not dq:
        dq.append((buildings[i], i))
        answer.append(0)
        continue
    # 현재 빌딩이 가장 크다면 레이저가 닿을 수 없음
    if dq[0][0] < buildings[i]:
        answer.append(0)
        dq = deque([(buildings[i], i)])
    # 레이저가 닿을 수 있다면
    else:
        while dq:
            height, idx = dq.pop()
            if height >= buildings[i]:
                answer.append(idx + 1)
                dq.append((height, idx))
                break
        dq.append((buildings[i], i))
for idx in answer:
    print(idx, end=' ')

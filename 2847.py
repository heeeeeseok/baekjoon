n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))

answer = 0
before = scores[-1]
for i in range(len(scores) - 2, -1, -1):
    cur = scores[i]
    if cur >= before:
        scores[i] -= (cur - before + 1)
        answer += (cur - before + 1)
    before = scores[i]
print(answer)
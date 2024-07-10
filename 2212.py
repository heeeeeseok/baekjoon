n = int(input())
k = int(input())
sensors = list(map(int, input().split()))
sensors = sorted(sensors)
dists = []
dist_sum = max(sensors) - min(sensors)

for i in range(1, len(sensors)):
    dists.append(abs(sensors[i] - sensors[i - 1]))
dists = sorted(dists, reverse=True)

answer = dist_sum
for i in range(min(k - 1, len(dists))):
    answer -= dists[i]
print(answer)

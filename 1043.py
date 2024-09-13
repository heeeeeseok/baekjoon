def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
knows = list(map(int, input().split()))
# 아무도 진실을 모를 때, 파티 개수 출력
if knows[0] == 0:
    print(m)
    exit()

answer = 0
parent = [i for i in range(n + 1)]
parties = []
for i in range(m):
    people = list(map(int, input().split()))
    parties.append(people)
    for person in people[2:]:
        union(people[1], person)

for party in parties:
    result = []
    flag = True
    for know in knows[1:]:
        if find(party[1]) == find(know):
            flag = False
            break
    if flag:
        answer += 1
print(answer)

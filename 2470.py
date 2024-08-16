import sys
input = sys.stdin.readline
MAX = 1000000001


n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
answer1 = MAX
answer2 = MAX
for i in range(n):
    target = -liquids[i]
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if liquids[mid] == target:
            print(liquids[i], liquids[mid])
            exit()
        elif liquids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left != n and left != i:
        if abs(answer1 + answer2) > abs(liquids[i] + liquids[left]):
            answer1 = min(liquids[i], liquids[left])
            answer2 = max(liquids[i], liquids[left])
    if right != i:
        if abs(answer1 + answer2) > abs(liquids[i] + liquids[right]):
            answer1 = min(liquids[i], liquids[right])
            answer2 = max(liquids[i], liquids[right])
print(answer1, answer2)


n, k = map(int, input().split())
nums = list(map(int, input().split()))
appliance_d = dict()  # key: 전기용품, value: 개수
for num in nums:
    if appliance_d.get(num, 0):
        appliance_d[num] += 1
    else:
        appliance_d[num] = 1

# 가전제품의 개수가 멀티탭 구멍의 개수보다 적거나 같을 때 천처리
if len(appliance_d.keys()) <= n:
    print(0)
    exit()

multitap = []  # 멀티탭에 꽂힌 전기용품 번호 저장
answer = 0
INF = 987654321
for i in range(len(nums) - 1):
    # 멀티탭에 공간이 있을 떄
    if len(multitap) < n:
        if nums[i] not in multitap:
            multitap.append(nums[i])
    # 멀티탭에 공간이 없고 꽂혀있는 전기용품이 아닐 때
    elif len(multitap) == n and nums[i] not in multitap:
        app = []
        after = nums[i + 1:]
        for num in multitap:
            after_idx = INF
            if num in after:
                after_idx = after.index(num)
            app.append((-after_idx, num))
        app = sorted(app)
        multitap.remove(app[0][1])
        answer += 1
        multitap.append(nums[i])
if nums[-1] not in multitap:
    answer += 1
print(answer)

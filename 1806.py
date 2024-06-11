def solve():
    left = 0
    right = 0
    cur_sum = 0
    while cur_sum < s and right < n:
        cur_sum += nums[right]
        right += 1
    if cur_sum < s:  # 모두 더해도 S보다 작은 경우
        print(0)
        return

    answer = right - left  # 현재 S를 넘는 부분합의 길이
    while left < n:
        if cur_sum < s and right < n:
            cur_sum += nums[right]
            right += 1
        else:
            cur_sum -= nums[left]
            left += 1
        if cur_sum >= s:
            answer = min(answer, right - left)
    print(answer)
    return


n, s = map(int, input().split())
nums = list(map(int, input().split()))
solve()


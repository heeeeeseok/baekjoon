# S는 1 이상의 정수
# 원하는 위치의 수를 최대 K번 삭제 가능
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
cur_len = 0
answer = 0
left_k = k
while left <= right:
    if right == n:
        break

    # right가 짝수라면 현재 길이 증가
    if nums[right] % 2 == 0:
        cur_len += 1
        answer = max(answer, cur_len)
        right += 1
    # right가 홀수이고 k 횟수가 남아있다면 사용
    elif left_k > 0:
        right += 1
        left_k -= 1
    else:
        # left가 홀수인 경우 남은 k 횟수 증가
        if nums[left] % 2 == 1:
            left_k += 1
        # left가 짝수인 경우 현재 길이 감소
        else:
            cur_len -= 1
        left += 1

print(answer)

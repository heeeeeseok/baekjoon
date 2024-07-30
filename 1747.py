import math
n = int(input())

def is_palindrome(num):
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    end = len(num_list)
    for i in range(end // 2):
        if num_list[i] != num_list[end - 1]:
            return False
        end -= 1
    return True


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


while True:
    if is_palindrome(n):
        if is_prime(n):
            print(n)
            break
    n += 1

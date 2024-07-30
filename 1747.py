import math
n = int(input())

def is_palindrome(num):
    num_list = list(str(num))
    for i in range(len(num_list)):
        if num_list[i] != num_list[-i - 1]:
            return False
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

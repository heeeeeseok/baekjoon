def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

x, y = map(int, input().split())
if x > y:
    x, y = y, x

print(x + y - gcd(y, x))

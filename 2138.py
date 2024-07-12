import sys
input = sys.stdin.readline


def switch(i):
    global xor_bulbs
    xor_bulbs[i] ^= 1
    if i - 1 >= 0:
        xor_bulbs[i - 1] ^= 1
    if i + 1 < n:
        xor_bulbs[i + 1] ^= 1

def check():
    for i in range(n):
        if xor_bulbs[i] == 1:
            return False
    return True


n = int(input())
bulbs = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))
xor_bulbs = [0] * n
for i in range(n):
    xor_bulbs[i] = bulbs[i] ^ target[i]

# 첫 번째 스위치를 고정
answer = 0
if xor_bulbs[0] == 1:
    answer += 1
    switch(1)
for i in range(2, n):
    if xor_bulbs[i - 1] == 1:
        answer += 1
        switch(i)

if check():
    print(answer)
    exit()

for i in range(n):
    xor_bulbs[i] = bulbs[i] ^ target[i]
# 첫 번째 스위치를 켰을 때
switch(0)
answer = 1
for i in range(1, n):
    if xor_bulbs[i - 1] == 1:
        answer += 1
        switch(i)

if check():
    print(answer)
else:
    print(-1)


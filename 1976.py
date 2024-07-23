def is_connected(a, b, visited):
    if board[a][b] == 1:
        return True
    for i in range(n):
        if board[a][i] == 1 and i not in visited:
            visited.append(i)
            if is_connected(i, b, visited):
                return True
    return False


n = int(input())
m = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
for i in range(n):
    board[i][i] = 1

travel = list(map(int, input().split()))

before_city = travel[0] - 1
for i in range(1, len(travel)):
    cur_city = travel[i] - 1
    if is_connected(before_city, cur_city, [before_city]):
        before_city = cur_city
    else:
        print("NO")
        exit()
print("YES")

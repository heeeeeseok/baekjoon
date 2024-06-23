def backtracking():
    global board
    for y in range(9):
        for x in range(9):
            # 정해지지 않은 숫자가 있다면
            if board[y][x] == 0:
                possible_nums = get_possible_nums(y, x)
                # 가능한 숫자가 없음. 백트래킹
                if not possible_nums:
                    return False
                # 가능한 모든 숫자로 테스트
                for num in possible_nums:
                    board[y][x] = num
                    if backtracking():
                        return True
                    # 실패했다면 다시 0을 할당
                    board[y][x] = 0
                # 가능한 모든 숫자가 실패한 경우. 백트래킹
                if board[y][x] == 0:
                    return False
    # board의 모든 값이 0이 아니라면 종료
    return True


def get_possible_nums(row, col):
    possible_nums = [i for i in range(1, 10)]
    # 행 체크
    for x in range(9):
        if board[row][x] in possible_nums:
            possible_nums.remove(board[row][x])
    # 열 체크
    for y in range(9):
        if board[y][col] in possible_nums:
            possible_nums.remove(board[y][col])
    # 3 x 3 영역 체크
    row_start = row - (row % 3)
    col_start = col - (col % 3)
    for y in range(row_start, row_start + 3):
        for x in range(col_start, col_start + 3):
            if board[y][x] in possible_nums:
                possible_nums.remove(board[y][x])
    return possible_nums


board = []
for i in range(9):
    board.append(list(map(int, input())))

backtracking()

for y in range(9):
    for j in range(9):
        print(board[y][j], end="")
    print()



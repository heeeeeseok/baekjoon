# () = 2
# [] = 3
# (x) = 2 x x
# [x] = 3 x x
# xy = x + y
def solve():
    answer = 0
    stack = []
    for c in input_list:
        if c not in ('(', ')', '[', ']'):
            return False
        if c in ('(', '['):
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            last = stack.pop()
            val = 0
            while stack and str(last).isdigit():
                val += last
                last = stack.pop()
            if last != '(':
                return False
            if val == 0:
                stack.append(2)
            else:
                stack.append(val * 2)
        elif c == ']':
            if not stack:
                return False
            last = stack.pop()
            val = 0
            while stack and str(last).isdigit():
                val += last
                last = stack.pop()
            if last != '[':
                return False
            if val == 0:
                stack.append(3)
            else:
                stack.append(val * 3)
        else:
            return False
    for elem in stack:
        if not str(elem).isdigit():
            return False
        else:
            answer += elem
    return answer


input_list = list(input().rstrip())
result = solve()
if not result:
    print(0)
else:
    print(result)

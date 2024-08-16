string = input()
explode = input()
stack = []
flag = True
for i in range(len(string)):
    char = string[i]
    if char not in explode:
        flag = False
        if stack:
            for j in range(len(stack)):
                print(stack[j], end='')
        print(char, end='')
        stack = []
        continue
    # 폭발 문자의 첫 문자일 때
    if char == explode[0]:
        stack.append(char)
        # 폭발 문자열 완성했다면 제거
        if stack[-1][0] == explode[-1]:
            for j in range(len(explode)):
                stack.pop()
    else:
        if stack:
            cur_idx = explode.index(char)
            top_idx = explode.index(stack[-1])
            # 다음 폭발문자가 들어올 때
            if top_idx + 1 == cur_idx:
                stack.append(char)
                # 폭발 문자열 완성했다면 제거
                if stack[-1] == explode[-1]:
                    for j in range(len(explode)):
                        stack.pop()
                continue
        # 순서가 잘못 들어온 경우
        flag = False
        if stack:
            for j in range(len(stack)):
                print(stack[j], end='')
        print(char, end='')
        stack = []
if stack:
    flag = False
    for j in range(len(stack)):
        print(stack[j], end='')
if flag:
    print('FRULA')
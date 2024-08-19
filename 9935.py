string = input()
explode = input()
stack = []
flag = True  # 출력이 없는 경우 체크
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
    # 폭발 문자의 첫 문자일 때 스택에 추가
    if char == explode[0]:
        stack.append(char)
        # 폭발 문자열을 완성했다면 제거
        if stack[-1] == explode[-1]:
            for j in range(len(explode)):
                stack.pop()
    else:
        if stack:
            cur_idx = explode.index(char)
            top_idx = explode.index(stack[-1])
            # 순서가 알맞게 들어온 경우
            if top_idx + 1 == cur_idx:
                stack.append(char)
                # 폭발 문자열을 완성헀다면 제거
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
# 스택에 남아있는 문자들 처리
if stack:
    flag = False
    for j in range(len(stack)):
        print(stack[j], end='')
# 출력이 한 번도 되지 않았을 때
if flag:
    print('FRULA')
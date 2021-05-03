def solution(s):
    answer = 0

    stack = []

    index = 0
    length = len(s)
    while index < length:
        if stack:
            if stack[-1] == s[index]:
                stack.pop()
            else:
                stack.append(s[index])
        else:
            stack.append(s[index])
        index += 1

    if stack:
        answer = 0
    else:
        answer = 1
    return answer

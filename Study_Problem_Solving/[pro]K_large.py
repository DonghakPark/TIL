from collections import deque

def solution(number, k):
    answer = ''

    num = deque(list(map(int, list(number))))

    stack = deque()
    count = k
    while count > 0 and num:
        now_num = num.popleft()

        while stack:
            if stack[-1] < now_num and count != 0:
                stack.pop()
                count -= 1
            else:
                stack.append(now_num)
                break
        if len(stack) == 0:
            stack.append(now_num)

    if count == 0:
        stack = stack + num
    else:
        for _ in range(count):
            stack.remove(min(stack))

    for element in stack:
        answer += str(element)

    return answer

if __name__ == "__main__":
    number = "4177252841"
    k = 4
    print(solution(number,k), "775841")
    print(solution("99991", 3), "99")
    print(solution("111119", 3), "119")
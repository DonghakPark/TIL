def solution(arrangement):
    answer = 0
    stick = list(arrangement)
    count = 0
    stick_count = 0
    for i in range(0, len(stick)):

        if len(stick) == 0:
            break;

        temp = stick.pop(0)

        if temp == '(' and stick[0] == ')':
            count = count + stick_count
            stick.pop(0)

        elif temp == '(':
            stick_count += 1
        elif temp == ')':
            stick_count -= 1
            count += 1

    answer = count
    return answer

if __name__=="__main__":
    arrangement = "()(((()())(())()))(())"
    print(solution(arrangement))

    arrangement2 = "(((())(())))"
    print(solution(arrangement2))
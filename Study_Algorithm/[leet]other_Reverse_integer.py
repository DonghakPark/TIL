def solution(x):
    if x >= 2**31-1 or x <= -2**31:
        return 0

    answer = ''
    minus = False

    x = str(x)

    for element in x:
        if element == '-':
            minus = True
        else:
            answer = element + answer
    answer = int(answer)
    if minus == True:
        answer = -1 * answer

    if answer >= 2**31-1 or answer <= -2**31:
        return 0

    return answer

if __name__=="__main__":
    x = 123
    print(solution(x))
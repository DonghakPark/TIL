def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num

    return answer
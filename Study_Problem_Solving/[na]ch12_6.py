"""
기둥과 보 설치 문제
author : donghak pakr
contact : donghark03@naver.com
"""


def check(answer):
    for element in answer:
        x, y, a = element
        if a == 0:
            if y == 0 or ([x, y - 1, 0] in answer) or ([x, y, 1] in answer) or ([x - 1, y, 1] in answer):
                continue
            return False
        else:
            if ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer) or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []

    while build_frame:
        x, y, a, b = build_frame.pop(0)
        if b == 0:
            answer.remove([x, y, a])
            if check(answer) is False:
                answer.append([x, y, a])

        elif b == 1:
            answer.append([x, y, a])
            if check(answer) is False:
                answer.remove([x, y, a])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer

if __name__ == "__main__":
    n = 5
    build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
    build_frame2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
    print(solution(n, build_frame))
    print(solution(n, build_frame2))

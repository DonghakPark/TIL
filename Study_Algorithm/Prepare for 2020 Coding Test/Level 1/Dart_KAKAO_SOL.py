import re
import math

"""
다시 한번 풀어 볼 것
"""

def solution(dartResult):
    bonus = { 'S' : 1, 'D' : 2, 'T' :3}
    option = { '' : 1, '*' : 2, '#' : -1}

    answer = 0

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(len(dart)):
        if dart[i][2] == '*' and i >0:
            dart[i-1] *= 2

        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] *option[dart[i][2]]

    answer = sum(dart)
    return answer


if __name__ == "__main__":
    result1 = "1S2D*3T"
    result2 = "1D2S#10S"

    print(solution(result1)) #answer = 37
    print(solution(result2)) #answer = 9
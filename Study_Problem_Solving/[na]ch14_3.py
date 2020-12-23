"""
실패율 문제
author : donghak park
contact : donghark03@naver.com
"""

def solution(N, stages):
    answer = []
    temp = []

    for i in range(1,N+1):
        try_people = 0
        stay = 0

        for element in stages:
            if element >= i:
                try_people += 1
                if element == i:
                    stay += 1

        if try_people == 0:
            temp.append([0,i])
        else:
            temp.append([(stay/try_people), i])


    temp.sort(key=lambda x:(-x[0],x[1]))
    for i in range(len(temp)):
        answer.append(temp[i][1])
    return answer

if __name__=="__main__":
    N = 5
    N2 = 4
    stages = [2,1,2,6,2,4,3,3]
    stages2 = [4,4,4,4,4]
    print(solution(N, stages))
    print(solution(N2, stages2))
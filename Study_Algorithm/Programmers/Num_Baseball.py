def solution(baseball):
    answer =0
    a = {}
    for i in range(1,11):
        a[i] = 0

    print(a)
    return answer

if __name__=="__main__":
    baseball = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
    print(solution(baseball))
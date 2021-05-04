def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
    return answer

if __name__=="__main__":
    print(solution(8, 1, 2), 1)
    print(solution(8, 2, 3), 2)
    print(solution(8, 4, 7), 3)
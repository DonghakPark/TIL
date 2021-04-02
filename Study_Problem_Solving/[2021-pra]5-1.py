def solution(n):
    answer = 0
    divisor = 5
    while divisor <= n:

        answer += n//divisor
        divisor *= 5

    return answer
if __name__=="__main__":
    print(solution(5))
    print(solution(10))
    print(solution(1203010023))
def solution(N,K):

    answer = 0

    while True:

        if N%K == 0:
            N = N//K
            answer += 1
        else:
            N = N -1
            answer += 1

        if N == 1:
            break

    return answer
def answer(N,K):
    n,k = map(int, input().split())
    result = 0

    while N >= K:
        while N%K != 0:
            N -=1
            result += 1
        N //= K
        result += 1

    while N > 1:
        N -=1
        result += 1

    print(result)

if __name__=="__main__":
    N = 25
    K = 5
    print(solution(N,K))
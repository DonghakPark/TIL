def solution(N):
    sqr = 2 ** N
    return (sqr + 1) ** 2

if __name__=="__main__":
    N = int(input())
    print(solution(N))
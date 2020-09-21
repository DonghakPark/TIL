def solution(N,M,K,number):
    answer = []
    number.sort(reverse=True)

    count = 0
    while True:

        if len(answer) == M:
            break

        if count == K:
            answer.append(number[1])
            count = 0
        else:
            answer.append(number[0])
            count += 1

    return sum(answer)

def answer():
    n,m,k = map(int,input().split())
    data = list(map(int,input().split()))

    data.sort()
    first = data[n-1]
    second = data[n-2]

    result = 0
    while True:
        for i in range(k):
            if m ==0:
                break
            result += first
            m -= 1
        if m ==0:
            break
        result += second
        m -= 1

    print(result)

if __name__=="__main__":
    N = 5
    M = 8
    K = 3
    number = [2,4,5,4,6]
    print(solution(N,M,K,number))
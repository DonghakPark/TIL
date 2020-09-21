def solution(N,M,arr):
    answer=0
    arr2 = []
    for i in range(len(arr)):
        arr2.append(min(arr[i]))

    answer = max(arr2)

    return answer

if __name__ == "__main__":
    N = 3
    M = 3
    arr =[[3,1,2],[4,1,4],[2,2,2]]
    print(solution(N,M,arr))

    arr = [[7,3,1,8],[3,3,3,4]]
    print(solution(N,M,arr))
def solution(n, times):
    answer = 0

    start = 1
    end = (len(times)+1) * max(times)

    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            end = mid - 1
        elif cnt < n:
            start = mid + 1

    return answer

if __name__=="__main__":
    n = 6
    times = [7,10]
    print(solution(n, times), 28)
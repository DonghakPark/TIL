"""
N-Queen 문제
author : donghak park
contact: donghark03@naver.com
TODO : 다시 풀어 볼 것 ( 골드 5 문제 )
"""

def is_possible(end):
    for i in range(1, end):
        if answer[end] == answer[i] or abs(answer[end]-answer[i]) == abs(end - i):
            return False
    return True

def solution(check):
    global count

    if check > N:
        count += 1

    else:
        for i in range(1, N+1):
            answer[check] = i
            if is_possible(check):
                solution(check + 1)

if __name__=="__main__":
    N = int(input())
    count = 0
    answer = [0 for _ in range(N+1)]

    solution(1)
    print(count)
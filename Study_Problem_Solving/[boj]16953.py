"""
A -> B 문제
author : donghak park
contact: donghark03@naver.com
"""
from collections import deque

def find_answer(A):
    visited = []

    Q = deque()
    Q.append([0,A])
    visited.append(A)

    while Q:
        count, num = Q.popleft()

        if num == B:
            return count + 1

        for next in (num * 2, int(str(num) + "1")):
            if next <= B:
                if next not in visited:
                    Q.append([count + 1, next])
                    visited.append(next)

    return -1

A, B = map(int, input().split())
answer = find_answer(A)
print(answer)


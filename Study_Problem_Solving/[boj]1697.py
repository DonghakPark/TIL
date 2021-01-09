"""
숨바꼭질 문제
author : donghak park
contact : donghark03@naver.com
"""

from collections import deque

L = 100001

def search(arr, N, K):
    Q = deque()
    Q.append(N)

    while Q:
        x = Q.popleft()

        if x == K:
            return arr[x]

        for j in (x + 1, x - 1, x * 2):
            if (0 <= j < L) and arr[j] == 0:
                arr[j] = arr[x] + 1
                Q.append(j)


N, K = map(int, input().split())
arr = [0] * L

answer = search(arr, N, K)
print(answer)

"""
숨바꼭질 2 문제
author : donghak park
contact: donghark03@naver.com
TODO : 다시 한번 풀어볼 것
"""
from collections import deque

def search(N):

    visited = [[-1, 0] for _ in range(100001)]
    answer = deque()
    answer.append(N)

    visited[N][0] = 0
    visited[N][1] = 1

    while answer:
        position = answer.popleft()

        for element in (position + 1, position - 1, position * 2):
            if 0 <= element <= 100000:
                if visited[element][0] == -1:
                    visited[element][0] = visited[position][0] + 1
                    visited[element][1] = visited[position][1]
                    answer.append(element)

                elif visited[element][0] == visited[position][0] + 1:
                    visited[element][1] += visited[position][1]

    return visited[K][0], visited[K][1]

N, K = map(int, input().split())

time, count = search(N)
print(time)
print(count)

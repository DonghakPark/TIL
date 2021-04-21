"""
뱀과 사다리 게임
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict
import heapq

N, M = map(int, input().split())

move = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    move[x] = y

Q = []
heapq.heappush(Q, [0,1])
answer = 1e9
visited = [0] * 101
visited[1] = 1

while Q:
    now_count, now = heapq.heappop(Q)

    if now == 100:
        answer = min(now_count, answer)
        break
    for i in range(1,7):
        if now + i < 101:
            if visited[now+i] == 0:
                if now+i in move.keys():
                    heapq.heappush(Q, [now_count+1, move[now+i]])
                    visited[move[now+i]] = 1
                else:
                    heapq.heappush(Q, [now_count + 1, now + i])
                    visited[now+i] = 1
print(answer)
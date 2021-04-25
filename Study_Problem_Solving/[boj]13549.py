# """
# 숨바꼭질 3 문제
# author : donghak park
# contact: donghark03@naver.com
# TODO : 다시 풀어볼 것 ( 골드 5 )
# """
# from collections import deque
#
# def search(N):
#
#     visited = [0] * 100001
#     Q = deque()
#     Q.append(N)
#
#     while Q:
#         position = Q.popleft()
#         if position == K:
#             return visited[position]
#
#         for next_position in (position + 1, position - 1, position * 2) :
#
#             if 0 <= next_position < 100001:
#                 if visited[next_position] == 0:
#                     if next_position == position * 2 and next_position != 0:
#                         visited[next_position] = visited[position]
#                         Q.appendleft(next_position)
#                     else:
#                         visited[next_position] = visited[position] + 1
#                         Q.append(next_position)
#
#
# N, K = map(int, input().split())
# answer = search(N)
# print(answer)
"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숨박꼭질3
description : 위상 정렬
"""

import heapq
import sys

input = sys.stdin.readline


def dijkstra():
    queue = []
    heapq.heappush(queue, (0, N))
    distance[N] = 0

    while queue:
        now_cost, now_position = heapq.heappop(queue)

        if now_position == K:
            return now_cost

        if distance[now_position] < now_cost:
            continue

        for next_position in [now_cost + 1, now_cost -1]:
            if 0 <= next_position < 100001:
                heapq.heappush(queue, (now_cost + 1, next_position))
                distance[next_position] = distance[now_position] + 1

        if now_position < K and now_position != 0:
            heapq.heappush(queue, (now_cost, now_position * 2))
            distance[now_position * 2] = distance[now_position]


N, K = map(int, input().split())
distance = [int(1e9)] * 200002
print(dijkstra())

"""
서강그라운드 문제
author : donghak park
contact: donghark03@naver.com
"""
INF = int(1e9)

N, M, R = map(int, input().split())
area_item = list(map(int, input().split()))
arr = [[INF] * N for _ in range(N)]

for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start-1][end-1] = min(arr[start-1][end-1], dist)
    arr[end-1][start-1] = min(arr[end-1][start-1], dist)

for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
            if a == b:
                arr[a][b] = 0

max_value = 0

for i in range(N):
    temp_value = 0
    for j in range(N):
        if arr[i][j] <= M:
            temp_value += area_item[j]

    max_value = max(max_value, temp_value)

print(max_value)

"""
위와 동일한 문제
dijkstra 알고리즘 문제 풀이
"""
# import heapq, sys
# INF = sys.maxsize
# input = sys.stdin.readline
#
# def dijkstra(S):
#
#     Q = []
#     distance = [INF] * (N+1)
#
#     heapq.heappush(Q, [0, S])
#     distance[S] = 0
#
#     while Q:
#         now_dist, now_vertex = heapq.heappop(Q)
#
#         for next_dist, next_vertex in arr[now_vertex]:
#             if next_dist + now_dist < distance[next_vertex]:
#                 next_dist += now_dist
#                 distance[next_vertex] = next_dist
#                 heapq.heappush(Q, [next_dist, next_vertex])
#
#     return distance
#
# N, M, R = map(int, input().split())
#
# area_item = list(map(int, input().split()))
# area_item.insert(0, 0)
#
# arr = [ [] for _ in range(N+1)]
#
# for _ in range(R):
#     start, end, dist = map(int, input().split())
#
#     arr[start].append([dist, end])
#     arr[end].append([dist, start])
#
# max_value = int(-1e9)
#
# for i in range(1, N+1):
#     temp_sum = 0
#     result = dijkstra(i)
#
#     for j in range(1,N+1):
#         if result[j] <= M:
#             temp_sum += area_item[j]
#
#     max_value = max(max_value, temp_sum)
#
# print(max_value)
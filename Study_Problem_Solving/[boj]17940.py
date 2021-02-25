"""
지하철 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import sys, heapq
input = sys.stdin.readline

def dijstra():
    Q = []
    distance = [int(1e9)] * N
    heapq.heappush(Q, [0,0])
    distance[0] = 0

    while Q:
        now_dist, now_vertex = heapq.heappop(Q)

        for next_dist, next_vertex in arr[now_vertex]:
            if distance[next_vertex] > now_dist + next_dist:
                next_dist += now_dist
                heapq.heappush(Q, [next_dist, next_vertex])
                distance[next_vertex] = next_dist

    return distance


N, M = map(int, input().split())

station = []
for i in range(N):
    station.append(int(input()))

station_map = [list(map(int,input().split())) for _ in range(N)]

arr = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if station_map[i][j] != 0:
            if abs(station[i]-station[j]) == 0:
                arr[i].append([station_map[i][j], j])
            else:
                arr[i].append([station_map[i][j]+int(1e6), j])

ret = dijstra()
print(ret[M]//int(1e6), ret[M]%int(1e6))

# 워셜 플루이드 풀이
# new_map = [[[0,0] for _ in range(N)] for _ in range(N)]
# # [환승 횟수, 시간]
#
# for i in range(N):
#     for j in range(N):
#         new_map[i][j][0] = abs(station[i] - station[j])
#         if station_map[i][j] == 0:
#             new_map[i][j][1] = int(1e9)
#             new_map[i][j][0] = int(1e9)
#
#         else:
#             new_map[i][j][1] = station_map[i][j]
#
# for a in range(N):
#     for b in range(N):
#         for k in range(N):
#             new_map[a][b] = min(new_map[a][b],
#                                 [new_map[a][k][0] + new_map[k][b][0], new_map[a][k][1] + new_map[k][b][1]])
#
# print(new_map[0][M][0], new_map[0][M][1])
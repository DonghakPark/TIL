"""
케빈 베이컨의 6단계 법칙
author : donghak park
contact : donghark03@naver.com
"""
INF = int(1e9)

N, M = map(int, input().split())

relation = [[INF] * N for _ in range(N)]

for i in range(N):
    relation[i][i] = 0

for _ in range(M):
    start, end = map(int, input().split())
    relation[start-1][end-1] = 1
    relation[end-1][start-1] = 1
for k in range(N):
    for a in range(N):
        for b in range(N):
            relation[a][b] = min(relation[a][b], relation[a][k]+relation[k][b])

answer = INF
index = INF
for i in range(len(relation)):
    if sum(relation[i]) < answer:
        answer = sum(relation[i])
        index = i
print(index+1)

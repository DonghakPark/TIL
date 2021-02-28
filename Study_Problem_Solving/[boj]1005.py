"""
ACM Craft 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict, deque
def topology_sort():
    DP_table = [0] * (N+1)

    q = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
            DP_table[i] += time_list[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            in_degree[i] -= 1
            DP_table[i] = max(DP_table[i], DP_table[now] + time_list[i])

            if in_degree[i] == 0:
                q.append(i)


    return DP_table[target]
T = int(input())

for test_case in range(T):

    N, K = map(int, input().split())
    time_list = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    in_degree = [0] * (N+1)

    for _ in range(K):
        start, end = map(int, input().split())
        graph[start].append(end)
        in_degree[end] += 1

    target = int(input())

    print(topology_sort())
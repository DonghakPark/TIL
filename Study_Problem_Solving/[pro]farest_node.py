import heapq

def dijstra(n, start, graph):
    Q = []
    distance = [int(1e9)] * (n+1)
    heapq.heappush(Q, [1,1])
    distance[1] = 0

    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        for next_cost, next_vertex in graph[now_vertex]:
            if now_cost + next_cost < distance[next_vertex]:
                next_cost += now_cost
                distance[next_vertex] = next_cost
                heapq.heappush(Q, [next_cost, next_vertex])
    return distance

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]

    for start, end in edge:
        graph[start].append([1,end])
        graph[end].append([1,start])

    ret = dijstra(n, 1, graph)
    max_ret = 0
    for element in ret:
        if element > max_ret and element != int(1e9):
            max_ret = element

    return ret.count(max_ret)

if __name__=="__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))

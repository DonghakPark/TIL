from collections import defaultdict, deque


def dijkstra(start, arr, N):
    distance = [int(1e9)] * (N + 1)

    Q = deque()
    Q.append([0, start])
    distance[1] = 0

    while Q:
        now_cost, now_vertex = Q.popleft()

        for new_cost, new_vertex in arr[now_vertex]:
            if now_cost + new_cost <= distance[new_vertex]:
                distance[new_vertex] = now_cost + new_cost
                Q.append([now_cost + new_cost, new_vertex])
    return distance


def solution(N, road, K):
    answer = 0

    new_arr = defaultdict(list)

    for start, end, cost in road:
        new_arr[start].append([cost, end])
        new_arr[end].append([cost, start])

    result = dijkstra(1, new_arr, N)
    for element in result:
        if element <= K:
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3), 4)

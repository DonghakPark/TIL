from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True

    while queue:

        v=queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

if __name__ == "__main__":
    graph = [
        [],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]
    ]

    visited_Q = [False] * 9
    visited_S = [False] * 9

    bfs(graph, 1, visited_Q)
    print("\n")
    dfs(graph, 1, visited_S)
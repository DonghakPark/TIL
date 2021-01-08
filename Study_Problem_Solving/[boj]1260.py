"""
DFS와 BFS 문제
author : donghak park
contact : donghark03@naver.com
"""

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


def BFS(graph, visited):

    Q = []
    temp = []
    for element in graph[V]:
        temp.append(element)
    temp.sort()
    for element in temp:
        Q.append(element)
    visited[V] = 1
    print(V, end= " ")
    while Q:
        ne = Q.pop(0)

        if visited[ne] == 0:
            visited[ne] = 1
            print(ne, end = " ")

            temp = []
            for element in graph[ne]:
                if visited[element] == 0:
                    temp.append(element)
            temp.sort()
            for element in temp:
                Q.append(element)

def DFS(graph, visited):

    stack = []
    temp = []
    for element in graph[V]:
        temp.append(element)
    temp.sort(reverse = True)
    for element in temp:
        stack.append(element)
    visited[V] = 1
    print(V, end=" ")

    while stack:
        ne = stack.pop()

        if visited[ne] == 0:
            visited[ne] = 1
            print(ne, end = " ")
            temp = []
            for element in graph[ne]:
                if visited[element] == 0:
                    temp.append(element)
            temp.sort(reverse= True)
            for element in temp:
                stack.append(element)

visited = [0] * (N+1)
DFS(graph, visited)
print()
visited = [0] * (N+1)
BFS(graph,visited)

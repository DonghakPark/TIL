# import heapq
# from collections import defaultdict
# import copy
#
# def search(start):
#     global gl_info
#     global graph
#
#     distance = [1e9] * (len(gl_info))
#
#     temp = set()
#     for i in range(len(gl_info)):
#         if gl_info[i] == 1:
#             temp.add(i)
#
#     wolf_list = [copy.deepcopy(temp) for _ in range(len(gl_info))]
#
#     Q = []
#
#     heapq.heappush(Q, [0, start, [], [start]])
#     distance[start] = 0
#     wolf_list[0] = set()
#
#     while Q:
#         now_cost, now_vertex, now_wolf, now_visited = heapq.heappop(Q)
#         print(Q)
#         next_wolf = set()
#         for element in now_wolf:
#             next_wolf.add(element)
#
#         for next_vertex in graph[now_vertex]:
#             if next_vertex in now_visited:
#                 break
#
#             next_cost = now_cost
#             next_visited = copy.deepcopy(now_visited)
#
#             if gl_info[next_vertex] == 1:
#                 next_cost += 1
#                 next_wolf.add(next_vertex)
#
#             if next_cost < distance[next_vertex]:
#                 distance[next_vertex] = next_cost
#                 if len(next_wolf) < len(wolf_list[next_vertex]):
#                     wolf_list[next_vertex] = copy.deepcopy(next_wolf)
#
#                 next_visited.append(next_vertex)
#                 heapq.heappush(Q, [next_cost, next_vertex, copy.deepcopy(next_wolf), copy.deepcopy(next_visited)])
#
#     return distance, wolf_list
#
# def solution(info, edges):
#     global answer
#     global graph
#     global gl_info
#     global now_s
#
#     answer = 0
#     gl_info = copy.deepcopy(info)
#     graph = defaultdict(list)
#
#     for edge in edges:
#         start, end = edge
#         if end not in graph[start]:
#             graph[start].append(end)
#         if start not in graph[end]:
#             graph[end].append(start)
#
#     take = [0 for _ in range(len(gl_info))]
#     take[0] = 1
#
#     now_s = 1
#     now_position = 0
#     visited_wolf = set()
#
#     while True:
#         flag = False
#
#         ret, ret_wolf = search(now_position)
#         print("pos ", now_position, "now_s", now_s)
#         print(ret_wolf)
#
#         for i in range(len(gl_info)):
#             if gl_info[i] == 0 and take[i] != 1:
#                 temp_cost = len(visited_wolf.union(ret_wolf[i]))
#                 if temp_cost < now_s:
#                     now_position = i
#                     take[i] = 1
#                     now_s += 1
#                     flag = True
#                     visited_wolf = visited_wolf.union(ret_wolf[i])
#                     break
#
#         if flag is False:
#             break
#     print(take)
#     answer = sum(take)
#     return answer
#
# if __name__ == "__main__":
#     print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]), 5)
#     print("----------------")
#     print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]),5)

import heapq
from collections import defaultdict
import copy

def search(cost, start):
    global gl_info
    global graph

    distance = [1e9] * (len(gl_info))
    Q = []

    heapq.heappush(Q, [cost, start])
    distance[start] = 0


    while Q:
        now_cost, now_vertex = heapq.heappop(Q)

        for next_vertex in graph[now_vertex]:
            next_cost = now_cost
            if gl_info[next_vertex] == 1:
                next_cost += 1
            if next_cost < distance[next_vertex]:
                distance[next_vertex] = next_cost
                heapq.heappush(Q, [next_cost, next_vertex])

    return distance

def solution(info, edges):
    global answer
    global graph
    global gl_info
    global now_s

    answer = 0
    gl_info = copy.deepcopy(info)
    graph = defaultdict(list)

    for edge in edges:
        start, end = edge
        if end not in graph[start]:
            graph[start].append(end)
        if start not in graph[end]:
            graph[end].append(start)

    take = [0 for _ in range(len(gl_info))]
    take[0] = 1

    now_s = 1
    now_position = 0
    now_cost = 0

    while True:
        flag = False
        ret  = search(now_cost, now_position)
        print("pos ", now_position, "cost ", now_cost)
        print(ret)

        for i in range(len(gl_info)):
            if gl_info[i] == 0 and ret[i] < now_s and take[i] != 1:
                now_position = i
                take[i] = 1
                now_s += 1
                flag = True
                break

        if flag is False:
            break
    print(take)
    answer = sum(take)
    return answer

if __name__ == "__main__":
    print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]), 5)
    print("----------------")
    print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]),5)
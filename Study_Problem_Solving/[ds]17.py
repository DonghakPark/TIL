# #스타트 택시
# from collections import deque
# answer =0
# N, M, oil = map(int, input().split())
#
# #지도
# arr_map = []
#
# #승객
# arr_ride = []
#
# for _ in range(N):
#     arr_map.append(list(map(int, input().split())))
#
# #택시 처음 위치
# x, y = map(int, input().split())
#
# for _ in range(M):
#     arr_ride.append(list(map(int, input().split())))
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def find(x1,y1, x2,y2):
#
#     if x1 == x2 and y1==y2:
#         return 0
#
#     #출발
#     x1 = x1 - 1
#     y1 = y1 - 1
#
#     #도착
#     x2 = x2 - 1
#     y2 = y2 - 1
#
#     visit = [[-1] * N for _ in range(N)]
#
#     Q = deque([])
#     Q.append([x1, y1])
#     visit[x1][y1] = 0
#     while Q:
#
#         r, c = Q.popleft()
#
#         for i in range(4):
#             nx = r + dx[i]
#             ny = c + dy[i]
#
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#
#             else:
#
#                 if visit[nx][ny] > visit[r][c] + 1:
#                     visit[nx][ny] = visit[r][c] + 1
#
#                 if visit[nx][ny] == -1 and arr_map[nx][ny] == 0:
#                     Q.append([nx,ny])
#                     visit[nx][ny] = visit[r][c] + 1
#
#     return visit[x2][y2]
#
# while arr_ride:
#
#     short = []
#
#     for element in arr_ride:
#         s_x, s_y, e_x, e_y = element
#
#         go = find(x,y, s_x,s_y)
#
#         short.append([s_x,s_y,e_x,e_y,go])
#
#     short.sort(key=lambda x:(x[4],x[0],x[1]))
#
#     s_x, s_y, e_x, e_y, go = short[0]
#
#     back = find(s_x, s_y, e_x, e_y)
#
#     total = go + back
#     # print("before", oil, total)
#     if oil - total >= 0:
#         oil -= total
#         oil += back*2
#         arr_ride.remove([s_x,s_y,e_x,e_y])
#         x,y = e_x,e_y
#
#     elif oil - total < 0:
#         oil = -1
#         break
#     # print("after:", oil)
# print(oil)

d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def find_passenger(_x_driver, _y_driver):
    global world_status, passenger_list, world_size
    available = [[1 for _ in range(world_size)] for __ in range(world_size)]
    stack = [[_x_driver, _y_driver]]
    _distance = 0
    available[_y_driver][_x_driver] = 0
    while stack:
        temp_stack = []
        passenger_candidates = []
        _distance += 1
        while stack:
            current_x, current_y = stack.pop()
            for direction in range(4):
                dx, dy = d[direction]
                next_x, next_y = current_x + dx, current_y + dy
                if 0 <= next_x < world_size and 0 <= next_y < world_size and available[next_y][next_x] and world_status[next_y][next_x] == 0:
                    available[next_y][next_x] = 0
                    temp_stack.append((next_x, next_y))
                    if passenger_list.get((next_x, next_y)):
                        passenger_candidates.append((next_x, next_y))
        if passenger_candidates:
            passenger_candidates.sort(key=lambda x: (x[1], x[0]))
            # print(_x_driver, _y_driver)
            # print(passenger_list)
            # print(passenger_candidates)
            _passenger_xy = passenger_candidates.pop(0)
            # print(_passenger_xy)
            # print()
            return [_passenger_xy, _distance]
        else:
            stack += temp_stack
    return [False, False]


def go_destination(_passenger_xy, _destination_xy):
    global world_status, passenger_list, world_size
    available = [[1 for _ in range(world_size)] for __ in range(world_size)]
    stack = [_passenger_xy]
    _distance = 0
    available[_passenger_xy[1]][_passenger_xy[0]] = 0
    while stack:
        temp_stack = []
        _distance += 1
        while stack:
            current_x, current_y = stack.pop()
            for direction in range(4):
                dx, dy = d[direction]
                next_x, next_y = current_x + dx, current_y + dy
                if 0 <= next_x < world_size and 0 <= next_y < world_size and available[next_y][next_x] and world_status[next_y][next_x] == 0:
                    if (next_x, next_y) == _destination_xy:
                        return _distance
                    else:
                        available[next_y][next_x] = 0
                        temp_stack.append((next_x, next_y))
        stack += temp_stack
    return False


world_size, passenger_count, fuel_stored = map(int, input().split())
# 0 이 빈칸 1이 벽
world_status = [list(map(int, input().split())) for _ in range(world_size)]
y_driver, x_driver = map(int, input().split())
y_driver -= 1
x_driver -= 1
passenger_list = {}
for _ in range(passenger_count):
    y1, x1, y2, x2 = map(int, input().split())
    passenger_list[(x1-1, y1-1)] = (x2-1, y2-1)

for passenger in range(len(passenger_list)):
    # 손님이 현재 택시 위치에 있는 지 확인해보기
    if passenger_list.get((x_driver, y_driver)):
        passenger_xy = (x_driver, y_driver)
        destination_xy = passenger_list[passenger_xy]
        distance = go_destination(passenger_xy, destination_xy)
        if distance == False:
            print(-1)
            break
        fuel_stored -= distance
        x_driver, y_driver = destination_xy
        # print("distance2: ", distance)

        # 연로가 음수이면 -1 리턴, 0 이상이면 (이동 거리 * 2를 잔여 연료에 더하고)
        if fuel_stored < 0:
            print(-1)
            break
        else:
            # pprint.pprint(world_status)
            # print(passenger_list)
            # print(passenger_xy)
            # print(" ======================= ")
            del passenger_list[passenger_xy]
            fuel_stored += distance * 2
    else:
        # 택시에서 제일 가까운 손님 찾기 BFS( + 택시로 손님까지 이동 거리 계산하고) - 동률일 때 계산!!
        passenger_xy, distance = find_passenger(x_driver, y_driver)
        if not passenger_xy:
            print(-1)
            break
        destination_xy = passenger_list[passenger_xy]
        fuel_stored -= distance
        # print("distance1: ", distance)

        # 택시로 도착지까지 이동하고 (BFS 돌리고 + 이동 거리 계산해두고)
        distance = go_destination(passenger_xy, destination_xy)
        if distance == False:
            print(-1)
            break
        fuel_stored -= distance
        x_driver, y_driver = destination_xy
        # print("distance2: ", distance)

        # 연로가 음수이면 -1 리턴, 0 이상이면 (이동 거리 * 2를 잔여 연료에 더하고)
        if fuel_stored < 0:
            print(-1)
            break
        else:
            # pprint.pprint(world_status)
            # print(passenger_list)
            # print(passenger_xy)
            # print(" ======================= ")
            del passenger_list[passenger_xy]
            fuel_stored += distance * 2
else:
    print(fuel_stored)

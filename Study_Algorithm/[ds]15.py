# 미세먼지 안녕

# R,C,T = map(int, input().split())
#
# ori = []
# for _ in range(R):
#     ori.append(list(map(int, input().split())))
#
# temp = [[0] * C for i in range(R)] #확산 후
# temp2 = [[0] * C for i in range(R)] #확산 후 순환
#
# time = 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# air = []
#
# for i in range(R):
#     for j in range(C):
#         if ori[i][j] == -1:
#             air.append([i,j])
#
# while time < T:
#
#     #확산 진행
#     for i in range(R):
#         for j in range(C):
#             count = 0
#
#             #공기 청정기 일 시
#             if ori[i][j] == -1:
#                 continue
#             else:
#                 for d in range(4):
#                     nx = i + dx[d]
#                     ny = j + dy[d]
#
#                     if nx < R and ny < C and nx >=0 and ny >=0 and ( [nx,ny] not in air ):
#                         temp[nx][ny] += int( ori[i][j]/5 )
#                         count += 1
#
#                 temp[i][j] += ori[i][j] - (int(ori[i][j]/5) * count)
#
#     #temp 가 1초후 확산된것
#     x1,y1 = air[0]
#     x2,y2 = air[1]
#
#     for i in range(R):
#         for j in range(C):
#
#             #뒤에서 부터 처리하기
#             if j == y1 and i < x1:
#                 temp2[i+1][j] = temp[i][j]
#             elif j == y2 and i > x2:
#                 temp2[i-1][j] = temp[i][j]
#
#             if i == 0 and j >0:
#                 temp2[i][j-1] = temp[i][j]
#
#             elif i == R-1 and j>0:
#                 temp2[i][j-1] = temp[i][j]
#
#             if j == C-1 and i >= x1:
#                 temp2[i-1][j] = temp[i][j]
#             elif j == C-1 and i <=x2:
#                 temp2[i+1][j] = temp[i][j]
#
#
#             #앞으로 나아갈 때
#             if i == x1 and j < C-1:
#                 temp2[i][j+1] = temp2[i][j]
#             elif i==x1 and j == C-1:
#                 temp2[i-1][j] = temp2[i][j]
#             elif i == x2 and j < C-1:
#                 temp2[i][j+1] = temp2[i][j]
#             elif i == x2 and j == C-1:
#                 temp2[i+1][j] = temp2[i][j]
#     time += 1
#     print(temp)
#     print(temp2)



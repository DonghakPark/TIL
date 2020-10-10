# # 잔디 깍기 문제
#
# TC = int(input())
#
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
#
# for test_case in range(1, TC+1):
#     N, M = map(int, input().split())
#
#     answer = True
#
#     garden = []
#
#     for _ in range(N):
#         garden.append(list(map(int, input().split())))
#
#     if N == 1 and M ==1:
#         answer = True
#
#     elif N == 1:
#         if len(set(garden)) == 1:
#             answer = True
#     elif M == 1:
#         temp = []
#         for i in range(N):
#             for j in range(M):
#                 temp.append(garden[i][j])
#         if len(set(garden)) == 1:
#             answer = True
#
#     else:
#         for i in range(1, N-1):
#             for j in range(1, M-1):
#
#                 ori = garden[i][j]
#                 count = 0
#                 for k in range(4):
#                     nx, ny = i + dx[k], j + dy[k]
#                     if garden[nx][ny] == ori:
#                         count +=1
#                     else:
#                         continue
#                 if count == 4:
#                     continue
#                 else:
#                     answer = False
#
#     if answer == False:
#         print("#{} {}".format(test_case, "NO"))
#     else:
#         print("#{} {}".format(test_case, "YES"))
#

def cuttable(M, N, ans):
    for j in range(N):
        for i in range(M):
            if not ans[j][i] in [max(ans[j]), max([ans[x][i] for x in range(N)])]:
                return 'NO'
    return 'YES'


test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    x = []
    for __ in range(N):
        x.append(list(map(int, input().split())))
    print('#' + str(_ + 1) + ' ' + str(cuttable(M, N, x)))
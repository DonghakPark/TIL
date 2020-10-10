# #경사로 문제
#
# def solution(N,L,arr):
#
#     answer = 0
#
#     row = arr
#     col = []
#
#     for j in range(N):
#         temp = []
#         for i in range(N):
#             temp.append(arr[i][j])
#         col.append(temp)
#
#     for i in range(N):
#         if find_path(i, L, row) is True:
#             answer += 1
#
#         if find_path(i, L, col) is True:
#             answer += 1
#
#     return answer
#
#
# def find_path(index, L, arr):
#
#     if len(set(arr[index])) == 1:
#         # 한줄이 모두 같은 수 일 경우
#         return True
#
#         #다룬 수가 있는 경우
#     else:
#         start = arr[index][0]
#         count = 0
#
#         for i in range(N):
#
#             if arr[index][i] == start:
#                 count += 1
#                 if i == N-1:
#                     return True
#             else:
#                 if abs(arr[index][i] - start) == 1:
#                     if count >= L:
#                         start = arr[index][i]
#                         count = 0
#
#                     else:
#                         return False
#                 else:
#                     return False
#
# if __name__=="__main__":
#     N, L = 6, 2
#     arr = [[3, 3, 3, 3, 3, 3],
#            [2, 3, 3, 3, 3, 3],
#            [2, 2, 2, 3, 2, 3],
#            [1, 1, 1, 2, 2, 2],
#            [1, 1, 1, 3, 3, 1],
#            [1, 1, 2, 3, 3, 2]]
#
#     print(solution(N,L,arr))


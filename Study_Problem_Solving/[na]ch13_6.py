"""
감시 피하기 문제
author : donghak park
contact : donghark03@naver.com
TODO : 다시 풀어보기
"""
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))

        if board[i][j] == 'X':
            spaces.append((i,j))

def watch(x,y,direction):
    if direction == 0:
        while y>= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == "O":
                return False
            y -=1

    if direction == 1:
        while y < n :
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            y += 1

    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "O":
                return False
            x += 1
    return False

def process():
    for x,y in teachers:

        for i in range(4):
            if watch(x,y,i):
                return True
    return False
find = False

for data in combinations(spaces, 3):
    for x,y in data:
        board[x][y] ="O"

    if not process():
        find = True
        break

    for x,y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")

# N = int(input())
# arr = []
#
# for _ in range(N):
#     trans = []
#     temp = input().split()
#     for element in temp:
#         if element == "X":
#             trans.append(0)
#         elif element == "S":
#             trans.append(1)
#         else:
#             trans.append(2)
#     arr.append(trans)
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# def search(x,y):
#     for i in range(4):
#         while True:
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 3:
#                 break
#             else:
#                 if arr[nx][ny] == 1:
#                     return False
#     return True
# Flag = True
# def bfs(count):
#     global Flag
#
#     if count == 3:
#
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] == 2:
#                     temp = search(i, j)
#                     if temp == False:
#                         Flag = False
#         return
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:
#                 arr[i][j] = 3
#                 count += 1
#                 bfs(count)
#                 arr[i][j] = 0
#                 count -= 1
#
# bfs(0)
# if Flag == True:
#     print("YES")
# else:
#     print("NO")

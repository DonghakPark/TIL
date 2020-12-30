"""
감시 피하기 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
arr = []

for _ in range(N):
    trans = []
    temp = input().split()
    for element in temp:
        if element == "X":
            trans.append(0)
        elif element == "S":
            trans.append(1)
        else:
            trans.append(2)
    arr.append(trans)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def search(x,y):
    for i in range(4):
        while True:
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] == 3:
                break
            else:
                if arr[nx][ny] == "1":
                    return False
    return True

def bfs(count):

    if count == 3:
        

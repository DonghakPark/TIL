"""
경사로 문제
author : donghak park
contact: donghark03@naver.com
"""

def check_possible(x, y, direct, col_row):
    #행 경사
    if col_row == 0:

        if direct == 0:
            if y-L < 0:
                return False
            else:
                for i in range(y-L, y):
                    if abs(arr[x][y] - arr[x][i]) != 1 or visited[x][i] != 0:
                        return False
        else:
            for i in range(y+1, y+L+1):
    #열 검사
    else:


def solution():

    visited = [[0] * N for _ in range(N)]
    answer = 0

    for i in range(N):
        flag = True
        for j in range(1, N-1):
            if arr[i][j] != arr[i][j-1]:
                if check_possible(i,j,0,0):
                    continue
                else:
                    flag = False
                    break
            elif arr[i][j] != arr[i][j+1]:
                if check_possible(i,j,1,0):
                    continue
                else:
                    flag = False
                    break
            else:
                continue

        if flag == True:
            answer += 1

    for j in range(N):
        flag = True
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                continue
            else:
                if check_possible(i,j,1):
                    continue
                else:
                    flag = False
                    break
        if flag == True:
            answer += 1


if __name__=="__main__":
    N, L = map(int, input().split())
    arr = [ list(map(int,input().split())) for _ in range(N) ]

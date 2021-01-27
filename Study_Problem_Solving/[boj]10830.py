"""
행렬 제곱 문제
author : donghak park
contact: donghark03@naver.com
"""
def multiply(arr, B):

    if B == 1:
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000
        return arr

    elif B % 2 == 1:

        arr2 = multiply(arr, B-1)
        result = []

        for i in range(N):
            temp = []
            for j in range(N):
                summ = 0
                for k in range(N):
                    row = arr2[i][k]
                    col = arr[k][j]
                    summ += row * col

                temp.append(summ % 1000)
            result.append(temp)

        return result

    else:

        arr2 = multiply(arr, B//2)
        result = []

        for i in range(N):
            temp = []

            for j in range(N):
                summ = 0

                for k in range(N):
                    row = arr2[i][k]
                    col = arr2[k][j]
                    summ += row * col

                temp.append(summ % 1000)
            result.append(temp)

        return result

import sys
input = sys.stdin.readline

N, B = map(int, input().split())

arr_ori = [list(map(int, input().split())) for _ in range(N)]

answer = multiply(arr_ori, B)

for i in range(N):
    for j in range(N):
        print(answer[i][j], end = " ")
    print()
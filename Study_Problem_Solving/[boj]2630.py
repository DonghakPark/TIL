"""
색종이 만들기 문제
author : donghak park
contact : donghark03@naver.com
"""


def check(arr2):
    length = len(arr2)
    first = arr2[0][0]

    for i in range(length):
        for j in range(length):
            if arr2[i][j] != first:
                return False
    return True


def solution(arr):
    global count_0
    global count_1

    if check(arr):
        if arr[0][0] == 1:
            count_1 += 1
            return True
        else:
            count_0 += 1
            return True
    else:
        div = len(arr)//2
        temp = []
        for i in range(2):
            start = (i) * div
            end = (i+1) * div
            new_arr = arr[start:end]

            for j in range(2):
                start_2 = (j) * div
                end_2 = (j+1) * div

                for element in new_arr:
                    temp.append(element[start_2:end_2])
                solution(temp)
                temp = []

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
count_0 = 0
count_1 = 0

solution(arr)
print(count_0)
print(count_1)
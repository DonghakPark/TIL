"""
쿼드트리 문제
author : donghak park
contact : donghark03@naver.com
"""

def check(arr):
    length = len(arr)

    first = arr[0][0]

    for i in range(length):
        for j in range(length):
            if arr[i][j] != first:
                return False
    return True

def solution(arr):

    if check(arr):
        if arr[0][0] == 0:
            print(0, end ="")
        else:
            print(1, end="")
    else:
        temp = []
        cut = len(arr) // 2
        print("(", end = "")
        for i in range(2):
            start = i * cut
            end = (i+1) * cut
            new_arr = arr[start:end]

            for j in range(2):
                start_2 = j * cut
                end_2 = (j+1) * cut

                for element in new_arr:
                    temp.append(element[start_2:end_2])

                solution(temp)
                temp = []
        print(")", end = "")

N = int(input())
arr = []
for _ in range(N):
    temp = list(input())
    arr.append(list(map(int, temp)))

solution(arr)



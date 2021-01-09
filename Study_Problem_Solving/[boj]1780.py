"""
종이의 개수 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
count_1 = 0 # -1
count_2 = 0 # 0
count_3 = 0 # 1
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

def all(arr):

    length = len(arr)
    A = arr[0][0]
    for i in range(length):
        for j in range(length):
            if A != arr[i][j]:
                return False
    return True

def check(arr):
    global count_1
    global count_2
    global count_3

    if all(arr):
        if arr[0][0] == -1:
            count_1 += 1
            return True
        elif arr[0][0] == 0:
            count_2 += 1
            return True
        elif arr[0][0] == 1:
            count_3 += 1
            return True
    else:
        length = len(arr)//3
        temp = []
        for i in range(3):
            start = length * i
            end = length * (i + 1)

            for j in range(3):

                start_2 = length * j
                end_2 = length * (j+1)
                new_arr = arr[start:end]

                for element in new_arr:
                    temp.append(element[start_2:end_2])
                check(temp)
                temp = []

check(arr)
print(count_1)
print(count_2)
print(count_3)
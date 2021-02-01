"""
N과 M (12) 문제
author : donghak park
contact: donghark03@naver.com
"""

def make_answer(start, count, arr2):
    global candidate

    if count >= M:
        if arr2 not in candidate:
            temp = []
            for element in arr2:
                print(element, end = " ")
                temp.append(element)
            print()
            candidate.append(temp)
            return
        else:
            return

    for i in range(start, N):
        arr2.append(arr[i])
        make_answer(i, count+1, arr2)
        arr2.remove(arr[i])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
candidate = []
make_answer(0, 0, [])
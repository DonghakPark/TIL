"""
N과 M 문제 (8)
author : donghak park
contact: donghark03@naver.com
"""

def make_answer(start, count, arr2):

    if count >= M:
        for element in arr2:
            print(element, end = " ")
        print()
        return

    for i in range(start, N):
        arr2.append(arr[i])
        make_answer(i, count+1, arr2)
        arr2.remove(arr[i])

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
make_answer(0, 0, [])

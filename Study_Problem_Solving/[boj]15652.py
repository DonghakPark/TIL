"""
N과 M (4) 문제
author : donghak park
contact: donghark03@naver.com
"""

def make_answer(count, arr):

    if count > M:
        for element in arr:
            print(element, end=" ")
        print()
        return

    for i in range(1, N+1):
        if len(arr) == 0:
            arr.append(i)
            make_answer(count + 1, arr)
            arr.remove(i)

        elif i >= arr[-1]:
            arr.append(i)
            make_answer(count + 1, arr)
            arr.remove(i)

N, M = map(int, input().split())

make_answer(1,[])
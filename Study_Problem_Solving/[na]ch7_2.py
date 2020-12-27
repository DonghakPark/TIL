"""
부품 찾기 문제
author : donghak park
contact : donghark03@naver.com
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
arr2 = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
    return None

for i in arr2:
    result = binary_search(arr, i, 0, N-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end=' ')


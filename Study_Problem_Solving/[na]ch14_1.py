"""
국영수 문제
author : donghak park
contact : donghark03@naver.com
"""
N = int(input())
arr = []
for i in range(N):
    name, kuk, eng, math = input().split()
    kuk, eng, math = int(kuk), int(eng), int(math)
    arr.append([name, kuk, eng, math])

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))
for element in arr:
    print(element[0])

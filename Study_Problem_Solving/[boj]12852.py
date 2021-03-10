"""
1로 만들기 2 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import deque

N = int(input())
Q = deque()
Q.append([N])
answer = []

while Q:
    arr = Q.popleft()

    x = arr[0]
    if x == 1:
        answer = arr
        break

    if x % 3 == 0:
        Q.append([x//3] + arr)

    if x % 2 == 0:
        Q.append([x//2]+arr)

    Q.append([x-1]+arr)

print(len(answer)-1)
for i in range(len(answer)-1, -1, -1):
    print(answer[i], end = " ")

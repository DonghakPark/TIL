"""
DSLR 문제
author : donghak park
contact : donghark03@naver.com
"""
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())

    visited = [0 for _ in range(10000)]

    Q = deque()
    Q.append([A,""])
    visited[A] = 1
    answer = ""

    while Q:

        target, instruction = Q.popleft()

        if target == B:
            answer = instruction
            break

        if 2*target <= 9999 and visited[2*target] == 0:
            visited[2*target] = 1
            Q.append([2*target, instruction + "D"])

        if 2 * target > 9999 and visited[(2 * target) % 10000] ==0:
            visited[(2*target) % 10000] = 1
            Q.append([(2*target)%10000, instruction + "D"])

        if target - 1 >= 0 and visited[target -1] == 0:
            visited[target - 1] = 1
            Q.append([target-1, instruction + "S"])

        if target -1 < 0 and visited[9999] == 0:
            visited[9999] = 1
            Q.append([9999, instruction + "S"])

        L_move = int((target % 1000) * 10 + target / 1000)
        if visited[L_move] == 0:
            visited[L_move] = 1
            Q.append([L_move, instruction+"L"])

        R_move = int((target % 10) * 1000 + target / 10)
        if visited[R_move] == 0:
            visited[R_move] = 1
            Q.append([R_move, instruction + "R"])

    print(answer)

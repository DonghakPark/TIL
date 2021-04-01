from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
top = deque(list(map(int, input().split())))
stack = []
answer = []
i = 0
while top:
    value, index = top.popleft(), i

    while stack:
        if stack[-1][0] > value:
            answer.append(stack[-1][1] + 1)
            stack.append([value, index])
            break
        else:
            stack.pop()

    if len(stack) == 0:
        answer.append(0)
        stack.append([value, index])
    i += 1

for element in answer:
    print(element, end = " ")

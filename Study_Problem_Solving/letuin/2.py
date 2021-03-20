# sol
# O(N)에 풀이 -> 해쉬 테이블 사용
# 테이블로 인덱스 처리 !

"""
TODO : O(N)으로 풀이해 볼 것 Complete

N = int(input())

ball_public = list(map(int, input().split()))
ball_private = list(map(int, input().split()))
ball_visited = [False] * N

answer = []
while ball_public:

    for i in range(N):
        if ball_visited[i] is False:
            if ball_private[i] == ball_public[0]:
                ball_visited[i] = True
                answer.append(ball_public.pop(0))
                break
            elif ball_private[i] == ball_public[-1]:
                ball_visited[i] = True
                answer.append(ball_public.pop())
                break
hit = 0
for i in range(N):
    if answer[i] == ball_private[i]:
        hit += 1

if hit == N:
    print(1)
elif hit == N-1:
    print(2)
elif hit == N-2:
    print(3)
else:
    print('꽝') #ASCII 코드 입력 안됨

for element in answer:
    print(element, end = " ")
"""

from collections import deque

N = int(input())
ball_public = deque(list(map(int, input().split())))
ball_private = list(map(int, input().split()))
ball_priority = {}
answer = []

for i in range(N):
    ball_priority[ball_private[i]] = i

while ball_public:
    if len(ball_public) == 1:
        answer.append(ball_public.pop())
    elif ball_priority[ball_public[0]] > ball_priority[ball_public[-1]]:
        answer.append(ball_public.pop())
    else:
        answer.append(ball_public.popleft())
hit = 0
for i in range(N):
    if answer[i] == ball_private[i]:
        hit += 1

if hit == N:
    print(1)
elif hit == N-1:
    print(2)
elif hit == N-2:
    print(3)
else:
    print('fail')

for element in answer:
    print(element, end = " ")
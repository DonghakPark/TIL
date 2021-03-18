# sol
# O(N)에 풀이 -> 해쉬 테이블 사용
# 테이블로 인덱스 처리 !

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

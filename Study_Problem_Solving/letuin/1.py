# sol

N, M = map(int, input().split())
cost_4 = []
cost_1 = []

for _ in range(M):
    temp_4, temp_1 = map(int, input().split())
    cost_4.append(temp_4)
    cost_1.append(temp_1)

A = N // 4
B = N % 4
cost_1.sort()
cost_4.sort()

if cost_1[0] * 4 < cost_4[0]:
    answer = (cost_1[0] * N)
elif cost_1[0] * B > cost_4[0]:
    answer = cost_4[0] * (A+1)
else:
    answer = (cost_4[0] * A) + (cost_1[0] * B)

print(answer)

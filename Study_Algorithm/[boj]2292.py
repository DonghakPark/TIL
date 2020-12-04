N = int(input())

answer = 0
K = 1
iteration = 0

while True:
    if N == 1:
        answer = 1
        break
    if K+1 <= N and N <= K + iteration:
        answer += 1
        break
    else:
        K = K + iteration
        iteration += 6
        answer += 1

print(answer)
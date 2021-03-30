import sys

N, K = map(int, input().split())
S = list(input())
visited = [False] * len(S)

answer = 0

for index in range(len(S)):
    if S[index] == "H":
        continue
    else:
        # 왼쪽 가장 먼 것 부터 오른쪽 까지
        start = 0
        end = index + K + 1
        if (index - K) >= 0:
            start = (index - K)
        if (index + K) >= N:
            end = N

        for index_arm in range(start, end):
            if S[index_arm] == "H" and visited[index_arm] is False:
                visited[index_arm] = True
                answer += 1
                break
print(answer)

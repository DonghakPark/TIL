"""
행복 유치원 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N, K = map(int, input().split())
person = list(map(int, input().split()))

diff = []
for i in range(N-1):
    diff.append(person[i+1] - person[i])
diff.sort()

answer = 0
for i in range(N-K):
    answer += diff[i]
print(answer)
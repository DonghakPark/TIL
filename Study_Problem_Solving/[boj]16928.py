"""
뱀과 사다리 게임
Author : DongHak Park
Contact: donghark03@naver.com
"""
from collections import defaultdict

N, M = map(int, input().split())

move = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    move[x] = y

dp_table = [1e9] * 101
for i in range(2,8):
    dp_table[i] = 1

for i in range(2,101):

    if i in move.keys():
        dp_table[move[i]] = dp_table[i]


    else:
        for j in range(1,7):
            if i+j > 100:
                break
            else:
                dp_table[i+j] = min(dp_table[i+j], dp_table[i] + 1)
print(dp_table[100])
"""
합분해 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

N, K = map(int, input().split())
dp_table = [[0] * 201 for i in range(201)]

for i in range(201):
    dp_table[i][1] = 1

for i in range(1, 201):
    for j in range(201):
        for k in range(j+1):
            dp_table[j][i] += dp_table[k][i-1]
print(dp_table[N][K] % 1000000000)
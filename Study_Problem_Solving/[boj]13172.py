"""
시그마 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""
import math

def make(x, k):
    if k == 1:
        return x
    if k & 1:
        return x * make(x, k - 1) % mod

    res = make(x, k // 2)
    return res * res % mod


M = int(input())

mod = 1000000007
answer = 0
for _ in range(M):
    a, b = map(int, input().split())
    c = math.gcd(a,b)
    b //= c
    a //= c
    inverse = make(a, mod - 2)
    answer += b * inverse % mod
    answer %= mod
print(answer)


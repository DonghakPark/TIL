import sys

p, n = map(int, input().split())
virus = list(map(int, input().split()))

total_virus = 0
while virus:
    now_virus = virus.pop(0)
    total_virus *= p
    total_virus %= 1000000007
    total_virus += now_virus

print(total_virus % 1000000007)
